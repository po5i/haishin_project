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

class Country(models.Model):
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=3,help_text='Ej: CL, AR, ...')
    tax = models.DecimalField(blank=True,null=True,max_digits=5, decimal_places=2)

    def __str__(self):
        return u''.join(self.name).encode('utf-8')

    class Meta:
        verbose_name_plural = "countries"
        ordering = ['name']

class City(models.Model):
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=3,help_text='Ej: SCL, BSAS, ...')
    country = models.ForeignKey(Country)
    
    def __str__(self):
        return u''.join(self.name).encode('utf-8')

    class Meta:
        verbose_name_plural = "cities"
        ordering = ['name']

class Town(models.Model):
    name = models.CharField(max_length=250)
    city = models.ForeignKey(City)

    def __str__(self):
        return u''.join(self.name).encode('utf-8')

    class Meta:
        ordering = ['name']

class Profile(models.Model):
    SOURCES = (
        ('braintree', 'braintree'),
        ('stripe', 'stripe'),
        ('manual', 'manual'),
    )
    user = models.OneToOneField(User)
    birth_date = models.DateField(blank=True,null=True)
    avatar = models.ImageField(upload_to=get_avatar_path,blank=True,null=True)
    country = models.ForeignKey(Country,blank=True,null=True)
    city = models.ForeignKey(City,blank=True,null=True)
    town = models.ForeignKey(Town,blank=True,null=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100,blank=True,null=True)
    source = models.CharField(max_length=200,blank=True,null=True,choices=SOURCES)
    #TODO: guardar informacion que braintree necesite

    def __str__(self):
        return u''.join((self.user.first_name," ",self.user.last_name)).encode('utf-8')


class BusinessCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return u''.join(self.name).encode('utf-8')

    class Meta:
        verbose_name_plural = "business categories"
        ordering = ['name']

class Business(models.Model):
    admin = models.ForeignKey(User)
    category = models.ForeignKey(BusinessCategory)
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to=get_business_path,blank=True,null=True)
    town = models.ForeignKey(Town)
    address = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100,blank=True,null=True)
    longitude = models.CharField(max_length=100,blank=True,null=True)
    phone = models.CharField(max_length=100,blank=True,null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0,blank=True,null=True)
    average_time = models.IntegerField(default=0)
    published = models.BooleanField(default=True)
    
    def __str__(self):
        return u''.join(("",self.name)).encode('utf-8')

    class Meta:
        verbose_name_plural = "businesses"
    
class DishCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return u''.join(self.name).encode('utf-8')

    class Meta:
        verbose_name_plural = "dish categories"
        ordering = ['name']

class Dish(models.Model):
    business = models.ForeignKey(Business)
    category = models.ForeignKey(DishCategory)
    name = models.CharField(max_length=100)
    tags = models.TextField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #photo = models.ImageField(upload_to=get_dish_path,blank=True,null=True)
    published = models.BooleanField(default=True)
    
    def __str__(self):
        return u''.join((self.name)).encode('utf-8')

    class Meta:
        verbose_name_plural = "dishes"

class Job(models.Model):
    MAIN_STATUSES = (
        ('Received', 'Received'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Shipped', 'Shipped'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    # SWIFT STATUSES
    #DELIVERY_STATUSES = (
    #    ('1', 'Unassigned'),
    #    ('2', 'Received'),
    #    ('4', 'Accepted'),
    #    ('5', 'PickedUp'),
    #    ('7', 'Completed'),
    #    ('0', 'Cancelled'),
    #)

    # SHIPPIFY STATUSES
    DELIVERY_STATUSES = (
        ('1', 'Getting ready'),
        ('2', 'Pending to assign'),
        ('3', 'Pending for shipper response'),
        ('4', 'Shipper confirmed'),
        ('5', 'Being picked up'),
        ('6', 'Being delivered'),
        ('7', 'Delivered successfully'),
        ('0', 'Cancelled'),
    )
    user = models.ForeignKey(User)
    business = models.ForeignKey(Business)
    timestamp = models.DateTimeField(auto_now_add=True)
    swift_job_id = models.CharField(max_length=512,blank=True,null=True)
    shippify_task_id = models.CharField(max_length=512,blank=True,null=True)
    payment_reference_id = models.CharField(max_length=512,blank=True,null=True)
    recipient_name = models.CharField(max_length=100,blank=True,null=True)
    recipient_address = models.CharField(max_length=100,blank=True,null=True)
    recipient_phone = models.CharField(max_length=100,blank=True,null=True)
    main_status = models.CharField(max_length=100,choices=MAIN_STATUSES)
    delivery_status = models.CharField(max_length=100,choices=DELIVERY_STATUSES)
    payment_status = models.CharField(max_length=100,blank=True,null=True)
    remarks = models.TextField(blank=True,null=True)

    class Meta:
        ordering = ['-timestamp']

class JobDetail(models.Model):
    job = models.ForeignKey(Job)
    dish = models.ForeignKey(Dish)

class JobStatusHistory(models.Model):
    job = models.ForeignKey(Job)
    main_status = models.CharField(max_length=100)
    delivery_status = models.CharField(max_length=100)

    