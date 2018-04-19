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
from MRBS.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',  HomeView.as_view(), name='home'),
    url(r'^car/$',  CarHomeView.as_view(), name='carhome'),
    url(r'^close/$', CloseView.as_view(), name='close'),

    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'^accounts/signin/$', auth_views.login,
        {'authentication_form': MyLoginForm,
         'template_name': 'registration/login.html',
         'redirect_field_name': 'home'}, name='login'),
    url(r'^account/password_change/$', auth_views.password_change,
		{'post_change_redirect' :'/',
		 'password_change_form': MyPasswordChangeForm }, name='password_change'),
    url(r'^account/profile/(?P<pk>[0-9]+)/edit/$', ProfileUpdateView.as_view(), name='edit_profile'),

    url(r'^booking/', include('booking.urls', namespace='booking')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^car/', include('car.urls', namespace='car')),
]
