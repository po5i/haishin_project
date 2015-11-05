import datetime
from haishin.models import *
from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from django.conf import settings
from django.core.mail import send_mail

class ProfileSerializer(serializers.ModelSerializer):
    get_chef_id = serializers.ReadOnlyField()    #Model property
    class Meta:
        model = Profile
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
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
    user = UserSerializer()
    class Meta:
        model = Business
        
class DishSerializer(serializers.ModelSerializer):
    business = BusinessSerializer()    
    class Meta:
        model = Dish

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        
class HistorySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    business = BusinessSerializer()
    class Meta:
        model = Job