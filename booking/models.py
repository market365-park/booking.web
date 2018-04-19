from __future__ import unicode_literals

from MRBS.settings import *
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class User(AbstractUser, ):
    phone = models.CharField(max_length=10, blank=True, null=True)

@python_2_unicode_compatible
class BookingInfo(models.Model):
    title = models.CharField('TITLE', max_length=50)
    room_id = models.CharField('ROOM', max_length=50, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, auto_created=True)
    start_time = models.DateTimeField('Start Time')
    end_time = models.DateTimeField('End Time')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)

    class Meta:
        verbose_name = 'booking'
        verbose_name_plural = 'bookings'
        ordering = ('-start_time',)

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class Room(models.Model):
    room_id = models.CharField('ROOM_ID', max_length=50)
    room_name = models.CharField('ROOM_NAME', max_length=50)
    event_color = models.CharField('COLOR', max_length=50)

    class Meta:
        verbose_name = 'room'
        verbose_name_plural = 'rooms'

    def __str__(self):
        return self.room_id
