from django.contrib import admin
from booking.models import *

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'room_name', 'event_color')

class BookingInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'room_id', 'owner', 'create_date')
    search_fields = ('title',)
    list_filter = ('room_id',)
    ordering = ('-start_time', 'room_id',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'phone', 'email')
    search_fields = ('first_name',)
    list_filter = ('last_name',)
    ordering = ('first_name', 'last_name', 'username',)
	
admin.site.register(User, UserAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(BookingInfo, BookingInfoAdmin)
