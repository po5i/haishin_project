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

# custom admins
class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )

class BusinessAdmin(admin.ModelAdmin):
    inlines = (DishInline, )

class CityAdmin(admin.ModelAdmin):
	inlines = (TownInline, )

class JobAdmin(admin.ModelAdmin):
	inlines = (JobDetailInline, JobStatusHistoryInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Our model
admin.site.register(Business, BusinessAdmin)
admin.site.register(BusinessCategory)
admin.site.register(DishCategory)
admin.site.register(Country)
admin.site.register(City, CityAdmin)
admin.site.register(Job, JobAdmin)