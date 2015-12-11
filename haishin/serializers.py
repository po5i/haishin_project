# -*- coding: utf-8 -*-
import datetime
from haishin.models import *
from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from django.conf import settings
from django.core.mail import send_mail
import json

import calendar
import shippify
import pusher_backend
import sendmails

import googlemaps
gmaps = googlemaps.Client(key=settings.GMAPS_API_CLIENT_KEY)

disablecss = True
sendmails.Email.set_configuration(settings.EMAIL_API_BASE_URL,settings.EMAIL_API_KEY, settings.EMAIL_FROM, disablecss)

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

        mail_sended = sendmails.Email.notify_update_profile(instance,profile)
       
        return instance

    class Meta:
        model = User
        write_only_fields = ('password',)

class BusinessCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessCategory


class BusinessSerializer(serializers.ModelSerializer):
    is_open = serializers.ReadOnlyField()    #Model property
    admin = UserSerializer()
    category = BusinessCategorySerializer()
    lookup_field = 'slug'
    extra_kwargs = {
        'url': {'lookup_field': 'slug'}
    }
    class Meta:
        model = Business

class DishCustomizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishCustomization

class DishAddonSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishAddon

class DishAddonCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DishAddonCategory

class DishSerializer(serializers.ModelSerializer):
    is_available = serializers.ReadOnlyField()    #Model property
    class Meta:
        model = Dish
    
    def to_representation(self, instance):
        ret = super(DishSerializer, self).to_representation(instance)

        items = DishCustomization.objects.filter(dish=instance)
        ret['customizations'] = []
        for item in items:
            serialized_detail = DishCustomizationSerializer(item).data
            ret['customizations'].append(serialized_detail)

        items = DishAddon.objects.filter(dish=instance)
        
        categories = {}
        for item in items:
            if not categories.has_key(item.category.id):
                categories[item.category.id] = DishAddonCategorySerializer(item.category).data
                categories[item.category.id]['items'] = []
            categories[item.category.id]['items'].append(DishAddonSerializer(item).data)

        #parse categories for better reading
        json_categories = []
        for key, items in categories.iteritems():
            json_categories.append(items)    
        
        ret['addons'] = json_categories

        return ret

    def to_internal_value(self, data):
        output = data
        try:
            output['business'] = Business.objects.get(id=data['business'])
            output['category'] = DishCategory.objects.get(id=data['category'])
        except:
            raise serializers.ValidationError({
                'business': 'Bad business or category id'
            })

        return output

    def create(self, validated_data):
        if "addons" in validated_data:
            addons = validated_data.pop('addons')
        else:
            addons = None

        # save the job
        dish = Dish.objects.create(**validated_data)

        # save the addons
        if addons:
            for addon in addons:
                addon_category = DishAddonCategory.objects.create(name=addon['name'],maximum=addon['maximum'])
                for item in addon['items']:
                    addon = DishAddon.objects.create(dish=dish,name=item['name'],price=item['price'],category=addon_category)

        return dish

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job

    shippify.Configuration.set_credentials(settings.SHIPPIFY_API_KEY, settings.SHIPPIFY_API_SECRET, settings.SHIPPIFY_DEBUG)
    pusher_backend.Pusher.init(settings.PUSHER_APP_ID, settings.PUSHER_KEY, settings.PUSHER_SECRET)

    # override in order to include 'details' field
    def to_internal_value(self, data):
        output = super(JobSerializer, self).to_internal_value(data)

        details = data.get('details')
        # Perform the data validation.
        if details:
            output["details"] = json.loads(details)

        return output

    def to_representation(self, instance):
        ret = super(JobSerializer, self).to_representation(instance)

        details = JobDetail.objects.filter(job=instance)
        ret['details'] = []
        for detail in details:
            serialized_detail = JobDetailSerializer(detail).data
            ret['details'].append(serialized_detail)

        history = JobStatusHistory.objects.filter(job=instance)
        ret['history'] = []
        for h in history:
            serialized_history = JobStatusHistorySerializer(h).data
            ret['history'].append(serialized_history)

        # Shippify task info
        try:
            response = shippify.Task.get_task(instance.shippify_task_id)
            ret['shippify'] = response
        except:
            ret['shippify'] = {}

        return ret

    def create_shippify(self,job):
        # integrate shippify API
        shippify_products = []  #id, name, qty, size=2
        job_details = JobDetail.objects.filter(job=job)
        for detail in job_details:
            shippify_products.append({
                    'id': detail.dish.id,
                    'name': detail.dish.name,
                    'qty': detail.quantity,
                    'size': 2
                })

        # parse delivery_date to EPOCH
        # (delivery_date is in UTC)
        if not job.delivery_date:
            job.delivery_date = datetime.datetime.now()
        unix_delivery_date = calendar.timegm(job.delivery_date.timetuple())

        api_data = {
            'task': {
                'products': shippify_products,
                'recipient': {
                    'name': job.recipient_name,
                    'email': job.user.email,
                    'phone': job.recipient_phone
                },
                'sender': {
                    'name': job.business.name,
                    'email': job.business.admin.email,
                    'phone': job.business.phone
                },
                'pickup': {
                    'address': job.business.address,
                    'lat': job.business.latitude,
                    'lng': job.business.longitude
                },
                'deliver': {
                    'address': job.recipient_address,
                    'lat': job.recipient_latitude,
                    'lng': job.recipient_longitude
                },
                'extra': '{\"job_id\":\"%d\",\"source\":\"DeliDelux\",\"debug\":\"%s\"}' % (job.id, settings.DEBUG) ,
                'payment_type': 1,
                'payment_status': 2,
                'total_amount': 0,
                'delivery_date': unix_delivery_date
            }
        }

        try:
            response = shippify.Task.create_task(api_data)
            job.shippify_task_id = response['id']
            job.shippify_distance = response['distance']
            job.shippify_price = response['price']
            job.save()
        except Exception as e:
            msg = "Shippify API ERROR: %s" % str(e)
            if not settings.SHIPPIFY_DEBUG:
                job.delete()
                raise serializers.ValidationError(msg)
            else:
                print " !!! " + msg


    def create(self, validated_data):
        if "details" in validated_data:
            details = validated_data.pop('details')
        else:
            details = None

        # save the job
        job = Job.objects.create(**validated_data)

        # save the details
        try:
            total = 0
            if details:
                for detail in details:
                    dish = Dish.objects.get(id=detail["dish"])
                    total = total + dish.price
                    job_detail = JobDetail.objects.create(job=job,dish=dish,quantity=detail["quantity"])

                    # save the addons
                    if "addons" in detail:
                        for addon in detail["addons"]:
                            dish_addon = DishAddon.objects.get(id=addon.get("id"))
                            total = total + dish_addon.price
                            JobDetailAddon.objects.create(job_detail=job_detail,addon=dish_addon,price=dish_addon.price)
        except Exception as e:
            job.delete()
            raise serializers.ValidationError({
                'addons': str(e)
            })

        # save the status history
        JobStatusHistory.objects.create(job=job,main_status=job.main_status,delivery_status=job.delivery_status)

        return job

    def update(self, instance, validated_data):
        new_main_status = validated_data.get('main_status', instance.main_status)
        new_delivery_status = validated_data.get('delivery_status', instance.delivery_status)

        if instance.main_status == 'Draft' and new_main_status == 'Received':
            # send task to shippify
            pusher_backend.Pusher.message('delidelux','restaurant_' + str(instance.business.id),'Hey!, Hay un nuevo pedido para tu negocio :)')
            mail_sended = sendmails.Email.notify_business_new_job(instance)
        elif instance.main_status == 'Received' and new_main_status == 'Accepted':
            # braintree submit for settlement
            self.create_shippify(instance)
            try:
                PaymentMethod.objects.get(job=instance).submit_for_settlement()
            except Exception as e:
                print "PaymentMethod submit for settlement error: %s" % str(e)
                #raise serializers.ValidationError({
                #    'paymentMethod': str(e)
                #})

            mail_sended = sendmails.Email.notify_client_job_accepted(instance)
            pusher_backend.Pusher.message('delidelux','user_' + str(instance.user.id),'Ya estamos cocinando tu pedido hecho en ' + str(instance.business.name))

        elif instance.main_status == 'Accepted' and new_main_status == 'Rejected':
            mail_sended = sendmails.Email.notify_client_job_rejected(instance)
            pusher_backend.Pusher.message('delidelux','user_' + str(instance.user.id),'Malas noticias, tu pedido hecho en ' + str(instance.business.name) + ' no puede ser aceptado.')

        elif new_delivery_status == '4':
            # Habemus motorizado... avisar a alguien?
            pass

        elif instance.main_status == 'Accepted' and new_main_status == 'Shipped':
            mail_sended = sendmails.Email.notify_client_job_shipped(instance)
            pusher_backend.Pusher.message('delidelux','user_' + str(instance.user.id),'Tu pedido hecho en ' + str(instance.business.name) + ' va en camino.')

        elif new_delivery_status == '5':
            new_main_status = 'Shipped'
            mail_sended = sendmails.Email.notify_client_job_shipped(instance)
            pusher_backend.Pusher.message('delidelux','user_' + str(instance.user.id),'Tu pedido hecho en ' + str(instance.business.name) + ' va en camino.')

        elif new_delivery_status == '6':
            pusher_backend.Pusher.message('delidelux','user_' + str(instance.user.id),'Tu pedido hecho en ' + str(instance.business.name) + ' esta por llegar.')

        elif new_delivery_status == '7':
            mail_sended = sendmails.Email.notify_client_job_completed(instance)
            new_main_status = 'Completed'

        elif new_main_status == 'Cancelled':
            # desición del negocio de cancelar la orden?
            pass

        elif new_delivery_status == '0' and (instance.main_status != 'Cancelled' or new_main_status != 'Cancelled'):
            # tenemos serios problemas aqui!
            # Shippify esta cancelando la orden
            pass




        # update the job
        instance.main_status = new_main_status
        instance.delivery_status = new_delivery_status
        instance.save()

        job = instance
        # save the status history
        JobStatusHistory.objects.create(job=job,main_status=job.main_status,delivery_status=job.delivery_status)

        return job

class SimpleDishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish

class JobDetailAddonSerializer(serializers.ModelSerializer):
    addon = DishAddonSerializer()
    class Meta:
        model = JobDetailAddon

class JobDetailSerializer(serializers.ModelSerializer):
    dish = SimpleDishSerializer()
    addons = JobDetailAddonSerializer(many=True)
    class Meta:
        model = JobDetail
        depth = 0

class JobStatusHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobStatusHistory

class DishCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DishCategory

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country

class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    lookup_field = 'slug'
    extra_kwargs = {
        'url': {'lookup_field': 'slug'}
    }
    class Meta:
        model = City

class TownSerializer(serializers.ModelSerializer):
    #country = CountrySerializer()
    class Meta:
        model = Town
