from django.db import models
from django.contrib.auth.models import User
import sys,os,time

#User._meta.get_field('email')._unique = True

def get_avatar_path(self,filename):
    filename = time.strftime("%Y%m%d-%H%M%S") + filename
    return os.path.join("avatar", "users", filename)
def get_business_path(self,filename):
    filename = time.strftime("%Y%m%d-%H%M%S") + filename
    return os.path.join("business", filename)
def get_dish_path(self,filename):
    filename = time.strftime("%Y%m%d-%H%M%S") + filename
    return os.path.join("dishes", filename)

class Profile(models.Model):
    user = models.OneToOneField(User)
    birth_date = models.DateField(blank=True,null=True)
    avatar = models.ImageField(upload_to=get_avatar_path,blank=True,null=True)
    country = models.CharField(max_length=100,blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return u''.join((self.user.first_name," ",self.user.last_name)).encode('utf-8')
    
class Business(models.Model):
    admin = models.OneToOneField(User)
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to=get_business_path,blank=True,null=True)
    country = models.CharField(max_length=100,blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100,blank=True,null=True)
    published = models.BooleanField(default=True)
    
    def __str__(self):
        return u''.join(("",self.user.username)).encode('utf-8')
    
class Dish(models.Model):
    business = models.ForeignKey(Business)
    name = models.CharField(max_length=100)
    tags = models.TextField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    #photo = models.ImageField(upload_to=get_dish_path,blank=True,null=True)
    published = models.BooleanField(default=True)
    
    def __str__(self):
        return u''.join((self.name)).encode('utf-8')

class Job(models.Model):
    MAIN_STATUSES = (
        ('Received', 'Received'),
        ('Accepted', 'Accepted'),
        ('Delivered', 'Delivered'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    SWIFT_STATUSES = (
        ('Received', 'Received'),
        ('Accepted', 'Accepted'),
        ('PickedUp', 'PickedUp'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    user = models.ForeignKey(User)
    business = models.ForeignKey(Business)
    timestamp = models.DateTimeField(auto_now_add=True)
    swift_api_id = models.CharField(max_length=512,blank=True,null=True)
    payment_reference_id = models.CharField(max_length=512,blank=True,null=True)
    recipient_name = models.CharField(max_length=100,blank=True,null=True)
    recipient_address = models.CharField(max_length=100,blank=True,null=True)
    recipient_phone = models.CharField(max_length=100,blank=True,null=True)
    main_status = models.CharField(max_length=100,choices=MAIN_STATUSES)
    delivery_status = models.CharField(max_length=100,choices=SWIFT_STATUSES)
    payment_status = models.CharField(max_length=100,blank=True,null=True)
    