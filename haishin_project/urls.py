""" URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers
from haishin.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

#routers 
router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'dish', DishViewSet, 'dish')
router.register(r'city', CityViewSet, 'city')
router.register(r'business', BusinessViewSet, 'business')
router.register(r'job', JobViewSet, 'job')


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='haishin.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    
    url(r'^api-token/login/(?P<backend>[^/]+)/$', ObtainAuthToken.as_view()),
    url(r'^api-token/reset/', ResetPassword.as_view()),
    #url(r'^api-token/user/', ObtainUser.as_view()),
    url(r'^api-token/logout/', ObtainLogout.as_view()),
    url(r'^util/distance/', DistanceMatrix.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
