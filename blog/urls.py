"""MRBS_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from booking.forms import MyLoginForm, MyPasswordChangeForm
from blog.views import *

urlpatterns = [
    url(r'^$', PostLV.as_view(), name='main'),
    # Example: /post/ (same as /)
    url(r'^post/$', PostLV.as_view(), name='post_list'),

    # Example: /post/django-example/
    url(r'^post/(?P<pk>\d+)/$', PostDV.as_view(), name='post_detail'),

    # Example: /archive/
    url(r'^archive/$', PostAV.as_view(), name='post_archive'),

    # Example: /2012/
    url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),

    # Example: /2012/nov/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'),

    # Example: /2012/nov/10/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),

    # Example: /today/
    url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),

    # Example: /search/
    url (r'^search/$', SearchFormView.as_view(), name='search'),

    # Example: /bssearch/ (Bootstrap Search)
    url (r'^bssearch/$', BstrapSearchLV.as_view(), name='bssearch'),

    # Example: /add/
    url(r'^add/$', PostCreateView.as_view(), name="add"),

    # Example: /change/
    url(r'^change/$', PostChangeLV.as_view(), name="change"),

    # Example: /99/update/
    url(r'^(?P<pk>[0-9]+)/update/$', PostUpdateView.as_view(), name="update"),

    # Example: /99/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$', PostDeleteView.as_view(), name="delete"),
]
