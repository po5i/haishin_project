import datetime
from haishin.models import *
from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from django.conf import settings
from django.core.mail import send_mail
import json

class ProfileSerializer(serializers.ModelSerializer):
    get_chef_id = serializers.ReadOnlyField()    #Model property
    class Meta:
        model = Profile
        
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(partial=True)
    
    def to_internal_value(self, data):
        if User.objects.filter(email=data.get("email")).count() > 1:
            raise serializers.ValidationError({
                'email': 'User already exists'
            })
         
        output = data
        # Perform the data validation.
        if "profile" in data and "birth_date" in data["profile"] and data["profile"]["birth_date"] is not None:
            output["profile"]["birth_date"] = datetime.datetime.strptime(data["profile"]["birth_date"], '%Y-%m-%d').date()

        # Return the validated values. This will be available as
        # the `.validated_data` property.
        return output
    
    def create(self, validated_data):
        if "profile" in validated_data:
            profile_data = validated_data.pop('profile')
        else:
            profile_data = None

        user = User.objects.create(**validated_data)
        if user:
            user.set_password(user.password)
            user.save()
        if profile_data:
            Profile.objects.create(user=user, **profile_data)
        else:
            Profile.objects.create(user=user)
        return user

    
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile
        
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        if validated_data.get('password'):
            instance.set_password(validated_data.get('password'))
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        
        profile.birth_date = profile_data.get('birth_date', profile.birth_date)
        profile.country = profile_data.get('country', profile.country)
        profile.city = profile_data.get('city', profile.city)
        profile.address = profile_data.get('address', profile.address)
        profile.phone = profile_data.get('phone', profile.phone)
        profile.save()
        
        return instance

    class Meta:
        model = User
        write_only_fields = ('password',)

class BusinessSerializer(serializers.ModelSerializer):
    admin = UserSerializer()
    class Meta:
        model = Business
        
class DishSerializer(serializers.ModelSerializer):
    business = BusinessSerializer()
    class Meta:
        model = Dish

class SimpleDishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish

class JobSerializer(serializers.ModelSerializer):
    business = BusinessSerializer()

    class Meta:
        model = Job

    # override in order to include 'details' field
    def to_internal_value(self, data):
        output = super(JobSerializer, self).to_internal_value(data)
       
        details = data.get('details')
        # Perform the data validation.
        if not details:
            raise serializers.ValidationError({
                'details': 'This field is required.'
            })

        output["details"] = json.loads(details)
        return output

    def to_representation(self, instance):
        ret = super(JobSerializer, self).to_representation(instance)
        details = JobDetail.objects.filter(job=instance)
        ret['details'] = []
        for detail in details:
            serialized_detail = JobDetailSerializer(detail).data
            ret['details'].append(serialized_detail)
        #TODO: add tracking info here
        return ret

    def create(self, validated_data):
        if "details" in validated_data:
            details = validated_data.pop('details')
        else:
            details = None

        job = Job.objects.create(**validated_data)
        
        if details:
            for detail in details:
                JobDetail.objects.create(job=job,dish_id=detail["dish"])
        
        return job

class JobDetailSerializer(serializers.ModelSerializer): 
    dish = SimpleDishSerializer()
    class Meta:
        model = JobDetail

class HistorySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    business = BusinessSerializer()
    class Meta:
        model = Job

class CountrySerializer(serializers.ModelSerializer): 
    class Meta:
        model = Country

class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer()  
    class Meta:
        model = City