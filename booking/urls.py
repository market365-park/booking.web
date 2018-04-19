from django.conf.urls import url

from booking.views import *
from MRBS.views import CloseView

urlpatterns = [
    # Example: /search/
    url(r'^search/$', SearchFormView.as_view(), name='search'),

    # Example: /add/
    url(r'^add/$', BookingCreateView.as_view(), name='add'),

    # Example: /change/
    url(r'^change/$', BookingChangeLV.as_view(), name='change'),

    # Example: /99/update/
    url(r'^(?P<pk>[0-9]+)/update/$', BookingUpdateView.as_view(), name='update'),

    # Example: /99/delete/
    url(r'(?P<pk>[0-9]+)/delete/$', BookingDeleteView.as_view(), name='delete'),

    url(r'^undefined/delete/$', CloseView.as_view(), name='close'),

    url(r'^alert/$', AlertView.as_view(), name='alert'),

    url(r'^fail/$', FailView.as_view(), name='fail')
]
