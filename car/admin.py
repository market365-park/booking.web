from django.contrib import admin
from car.models import *

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_id', 'car_name', 'event_color')

class BookingCarInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'car_id', 'owner', 'create_date')
    search_fields = ('title',)
    list_filter = ('car_id',)
    ordering = ('-start_time', 'car_id',)

admin.site.register(Car, CarAdmin)
admin.site.register(BookingCarInfo, BookingCarInfoAdmin)
