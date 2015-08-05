"""fitClub URL Configuration

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
from django.conf.urls import include, url, patterns
from django.contrib import admin
from rest_framework import routers
from views import *
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# This will work if DEBUG is True

urlpatterns = [
    url(r'^', include('fitApi.urls')),
    url(r'^', include('fitAdmin.urls')),
    url(r'^misfit$',misfit),
    url(r'^misfit/auth',misfit_authrize),
    url(r'^misfit/notification',misfit_notification),
    url(r'^django-admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^login/$', login),
    url(r'^error/(.+)/$', error),
    url(r'^$', home),
#    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))


]
from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    )

urlpatterns += staticfiles_urlpatterns()
