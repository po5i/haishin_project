from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import sys,os,time
import datetime
import braintree

#User._meta.get_field('email')._unique = True

def get_avatar_path(self,filename):
    filename = time.strftime("%Y%m%d-%H%M%S") + filename
    return os.path.join("avatar", "users", filename)
def get_city_path(self,filename):
    filename = time.strftime("%Y%m%d-%H%M%S") + filename
    return os.path.join("city", filename)
def get_business_path(self,filename):
    filename = time.strftime("%Y%m%d-%H%M%S") + filename
    return os.path.join("business", filename)
def get_logo_path(self,filename):
    filename = time.strftime("%Y%m%d-%H%M%S") + filename
    return os.path.join("business", filename)
def get_business_cover_path(self,filename):
    filename = time.strftime("%Y%m%d-%H%M%S") + filename
    return os.path.join("business_cover", filename)
def get_dish_path(self,filename):
    filename = time.strftime("%Y%m%d-%H%M%S") + filename
    return os.path.join("dishes", filename)

class Country(models.Model):
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=3,help_text='Ej: CL, AR, ...')
    tax = models.DecimalField(blank=True,null=True,max_digits=10, decimal_places=2)
    average_delivery_time = models.IntegerField(blank=True,null=True,default=30,help_text='En minutos')
    privacy = models.TextField(blank=True,null=True)
    terms_conditions = models.TextField(blank=True,null=True)
    about = models.TextField(blank=True,null=True)

    def __str__(self):
        return u''.join(self.name).encode('utf-8')

    class Meta:
        verbose_name_plural = "countries"
        ordering = ['name']

class City(models.Model):
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=5,help_text='Ej: SCL, CABA, ...')
    country = models.ForeignKey(Country)
    image = models.ImageField(upload_to=get_city_path,blank=True,null=True)

    def __str__(self):
        return u''.join(self.name).encode('utf-8')

    class Meta:
        verbose_name_plural = "cities"
        ordering = ['name']

class Town(models.Model):
    name = models.CharField(max_length=250)
    city = models.ForeignKey(City)

    def __str__(self):
        return u''.join((self.name,' / ',self.city.name,' / ',self.city.country.name)).encode('utf-8')

    class Meta:
        ordering = ['city__country__name','city__name','name']

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

    def create_or_update_braintree_customer(self,nonce):
        try:
            result = braintree.Customer.update(str(self.user.id), {
                "payment_method_nonce": nonce
            })
            if result.is_success:
                return result.customer, "ok"
            else:
                return False, result.message
        except:
            result = braintree.Customer.create({
                "id": self.user.id,
                "first_name": self.user.first_name,
                "last_name": self.user.last_name,
                "email": self.user.email,
                "payment_method_nonce": nonce
            })
            if result.is_success:
                return result.customer, "ok"
            else:
                return False, result.message

    def get_braintree_customer(self):
        try:
            customer = braintree.Customer.find(str(self.user.id))
            return customer, "ok"
        except Exception as e:
            return False, str(e)

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
    logo = models.ImageField(upload_to=get_logo_path,blank=True,null=True)
    cover_image = models.ImageField(upload_to=get_business_cover_path,blank=True,null=True)
    town = models.ForeignKey(Town)
    address = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100,blank=True,null=True)
    longitude = models.CharField(max_length=100,blank=True,null=True)
    phone = models.CharField(max_length=100,blank=True,null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0,blank=True,null=True)
    average_time = models.IntegerField(default=0)
    price_range = models.IntegerField(default=0)
    published = models.BooleanField(default=True)
    closed = models.BooleanField(default=False)

    monday_opens = models.TimeField(blank=True,null=True,help_text=settings.TIME_ZONE)
    monday_closes = models.TimeField(blank=True,null=True,help_text=settings.TIME_ZONE)
    tuesday_opens = models.TimeField(blank=True,null=True,help_text=settings.TIME_ZONE)
    tuesday_closes = models.TimeField(blank=True,null=True,help_text=settings.TIME_ZONE)
    wednesday_opens = models.TimeField(blank=True,null=True,help_text=settings.TIME_ZONE)
    wednesday_closes = models.TimeField(blank=True,null=True,help_text=settings.TIME_ZONE)
    thursday_opens = models.TimeField(blank=True,null=True,help_text=settings.TIME_ZONE)
    thursday_closes = models.TimeField(blank=True,null=True,help_text=settings.TIME_ZONE)
    friday_opens = models.TimeField(blank=True,null=True,help_text=settings.TIME_ZONE)
    friday_closes = models.TimeField(blank=True,null=True,help_text=settings.TIME_ZONE)
    saturday_opens = models.TimeField(blank=True,null=True,help_text=settings.TIME_ZONE)
    saturday_closes = models.TimeField(blank=True,null=True,help_text=settings.TIME_ZONE)
    sunday_opens = models.TimeField(blank=True,null=True,help_text=settings.TIME_ZONE)
    sunday_closes = models.TimeField(blank=True,null=True,help_text=settings.TIME_ZONE)

    def __str__(self):
        return u''.join(("",self.name)).encode('utf-8')

    class Meta:
        verbose_name_plural = "businesses"

    @property
    def is_open(self):
        now = datetime.datetime.now().time()
        weekday = datetime.datetime.today().weekday()

        if weekday == 0 and self.monday_opens and self.monday_closes and self.monday_opens < now and now < self.monday_closes:
            return True
        elif weekday == 1 and self.tuesday_opens and self.tuesday_closes and self.tuesday_opens < now and now < self.tuesday_closes:
            return True
        elif weekday == 2 and self.wednesday_opens and self.wednesday_closes and self.wednesday_opens < now and now < self.wednesday_closes:
            return True
        elif weekday == 3 and self.thursday_opens and self.thursday_closes and self.thursday_opens < now and now < self.thursday_closes:
            return True
        elif weekday == 4 and self.friday_opens and self.friday_closes and self.friday_opens < now and now < self.friday_closes:
            return True
        elif weekday == 5 and self.saturday_opens and self.saturday_closes and self.saturday_opens < now and now < self.saturday_closes:
            return True
        elif weekday == 6 and self.sunday_opens and self.sunday_closes and self.sunday_opens < now and now < self.sunday_closes:
            return True
        else:
            return False

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

    available_from = models.TimeField(blank=True,null=True,help_text=settings.TIME_ZONE)
    available_to = models.TimeField(blank=True,null=True,help_text=settings.TIME_ZONE)

    def __str__(self):
        return u''.join((self.name)).encode('utf-8')

    class Meta:
        verbose_name_plural = "dishes"

    @property
    def is_available(self):
        now = datetime.datetime.now().time()

        if self.available_from and self.available_to and self.available_from < now and now < self.available_to:
            return True
        else:
            return False

class DishAddonCategory(models.Model):
    name = models.CharField(max_length=100)
    maximum = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return u''.join(self.name).encode('utf-8')

    class Meta:
        verbose_name_plural = "dish addon categories"
        ordering = ['name']

class DishCustomization(models.Model):
    dish = models.ForeignKey(Dish)
    name = models.CharField(max_length=100)
    options = models.TextField(blank=True,null=True,help_text="Opciones separadas con coma")

class DishAddon(models.Model):
    dish = models.ForeignKey(Dish, related_name="addons")
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(DishAddonCategory)

    def __str__(self):
        return u''.join(self.name).encode('utf-8')

class Job(models.Model):
    MAIN_STATUSES = (
        ('Draft', 'Draft'),
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
    shippify_distance = models.FloatField(blank=True,null=True)
    shippify_price = models.DecimalField(blank=True,null=True,max_digits=10, decimal_places=2)
    payment_reference_id = models.CharField(max_length=512,blank=True,null=True)
    recipient_name = models.CharField(max_length=100,blank=True,null=True)
    recipient_address = models.CharField(max_length=100,blank=True,null=True)
    recipient_phone = models.CharField(max_length=100,blank=True,null=True)
    recipient_latitude = models.CharField(max_length=100,blank=True,null=True)
    recipient_longitude = models.CharField(max_length=100,blank=True,null=True)
    main_status = models.CharField(max_length=100,choices=MAIN_STATUSES)
    delivery_date = models.DateTimeField()
    delivery_status = models.CharField(max_length=100,choices=DELIVERY_STATUSES)
    payment_status = models.CharField(max_length=100,blank=True,null=True)
    remarks = models.TextField(blank=True,null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['-timestamp']

class JobDetail(models.Model):
    job = models.ForeignKey(Job)
    dish = models.ForeignKey(Dish)
    quantity = models.IntegerField(default=1)

class JobDetailAddon(models.Model):
    job_detail = models.ForeignKey(JobDetail, related_name="addons")
    addon = models.ForeignKey(DishAddon)
    price = models.DecimalField(blank=True,null=True,max_digits=10, decimal_places=2)    #for history purposes

class JobStatusHistory(models.Model):
    job = models.ForeignKey(Job)
    main_status = models.CharField(max_length=100)
    delivery_status = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

class PaymentMethod(models.Model):
    user = models.ForeignKey(User)
    job = models.ForeignKey(Job)
    transaction_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=100)
    card = models.CharField(max_length=10,blank=True,null=True)
    last = models.CharField(max_length=5,blank=True,null=True)
    paypal_email = models.CharField(max_length=100,blank=True,null=True)

    def submit_for_settlement(self):
        result = braintree.Transaction.submit_for_settlement(str(self.transaction_id))
        if result.is_success:
            return True, "ok"
        else:
            return False, result.message
