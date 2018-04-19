from __future__ import unicode_literals

from MRBS.settings import *
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class BookingCarInfo(models.Model):
    title = models.CharField('TITLE', max_length=50)
    car_id = models.CharField('CAR', max_length=50, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, auto_created=True)
    start_time = models.DateTimeField('Start Time')
    end_time = models.DateTimeField('End Time')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    passenger = models.CharField('PASSENGERS', max_length=100)
    purpose = models.CharField('PURPOSE', max_length=100)
    destination = models.CharField('DESTINATION', max_length=50)

    class Meta:
        verbose_name = 'bookingcar'
        verbose_name_plural = 'bookingcars'
        ordering = ('-start_time',)

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class Car(models.Model):
    car_id = models.CharField('CAR_ID', max_length=50)
    car_name = models.CharField('CAR_NAME', max_length=50)
    event_color = models.CharField('CAR', max_length=50)

    class Meta:
        verbose_name = 'car'
        verbose_name_plural = 'cars'

    def __str__(self):
        return self.car_id
