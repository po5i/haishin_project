from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from haishin.models import *

# inlines
class ProfileInline(admin.StackedInline):
    #inlines = (UserStatInline, ) #django does not support nested inlines
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class DishInline(admin.StackedInline):
    model = Dish

class TownInline(admin.StackedInline):
    model = Town

class JobDetailInline(admin.StackedInline):
    model = JobDetail

class JobStatusHistoryInline(admin.StackedInline):
    model = JobStatusHistory

class DishCustomizationInline(admin.StackedInline):
    model = DishCustomization

class DishAddonInline(admin.StackedInline):
    model = DishAddon



# custom admins
class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )

class DishAdmin(admin.ModelAdmin):
    inlines = (DishCustomizationInline, DishAddonInline)

class BusinessAdmin(admin.ModelAdmin):
    inlines = (DishInline, )
    list_display = ('name', 'category', 'get_country', 'get_city', 'town')

    def get_country(self, obj):
        return obj.town.city.country
    def get_city(self, obj):
        return obj.town.city

class CityAdmin(admin.ModelAdmin):
    inlines = (TownInline, )

class JobAdmin(admin.ModelAdmin):
    inlines = (JobDetailInline, JobStatusHistoryInline, )
    list_display = ('timestamp', 'user', 'business', 'main_status', 'delivery_status')

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Our model
admin.site.register(Business, BusinessAdmin)
admin.site.register(BusinessCategory)
admin.site.register(DishAddonCategory)
admin.site.register(Dish, DishAdmin)
admin.site.register(DishCategory)
admin.site.register(Country)
admin.site.register(City, CityAdmin)
admin.site.register(Job, JobAdmin)
