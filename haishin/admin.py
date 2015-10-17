from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from haishin.models import *

# Register your models here.
class ProfileInline(admin.StackedInline):
    #inlines = (UserStatInline, ) #django does not support nested inlines
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class DishInline(admin.StackedInline):
    model = Dish


# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )

class BusinessAdmin(admin.ModelAdmin):
    inlines = (DishInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Business, BusinessAdmin)
admin.site.register(Job)
