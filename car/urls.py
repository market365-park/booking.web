from django.conf.urls import url

from car.views import *
from MRBS.views import CloseView

urlpatterns = [
    # Example: /add/
    url(r'^add/$', BookingCarCreateView.as_view(), name='add'),

    # Example: /change/
    url(r'^change/$', BookingCarChangeLV.as_view(), name='change'),

    # Example: /99/delete/
    url(r'(?P<pk>[0-9]+)/delete/$', BookingCarDeleteView.as_view(), name='delete'),

    url(r'^undefined/delete/$', CloseView.as_view(), name='close'),

    url(r'^alert/$', AlertCarView.as_view(), name='alert'),

    url(r'^fail/$', FailCarView.as_view(), name='fail')
]