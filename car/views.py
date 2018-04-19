# -*- encoding: utf-8 -*-
from car.forms import CreateCarForm
from car.models import BookingCarInfo

from datetime import datetime, timedelta, time
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.http.response import *
from MRBS.views import LoginRequiredMixin

import datetime, time

class BookingCarCreateView(LoginRequiredMixin, CreateView, ListView):
    model = BookingCarInfo
    form_class = CreateCarForm
    template_name = 'bookingcar_form.html'
    success_url = reverse_lazy('close')


    def get_initial(self):
        if self.request.POST:
            # print '----------------------------------------- sspark debug'
            # print self.request.POST.get('start')
            # return {'start': self.request.POST.get('start')}
            return

        elif self.request.GET:
            start_time = datetime.datetime.fromtimestamp(float(self.request.GET.get('start')[:-3]))
            start_time_formatted = start_time - timedelta(hours=9)
            end_time = datetime.datetime.fromtimestamp(float(self.request.GET.get('end')[:-3]))
            end_time_formatted = end_time - timedelta(hours=9)

            return {
                'title': self.request.GET.get("name") + " ("+ self.request.GET.get("team") + ", " + self.request.GET.get("phone") + ")",
                'start_time': start_time_formatted.strftime("%Y-%m-%d %H:%M"),
                'end_time': end_time_formatted.strftime("%Y-%m-%d %H:%M"),
                'car_id': self.request.GET.get("car")
            }

    def form_valid(self, form):
        bookingcarinfo_list = self.model.objects.all()
        date_format = '%Y-%m-%d %H:%M'

        new_start_time = str(self.request.POST['start_time'])
        new_start_day = new_start_time[:10]
        new_start_epoch = int(time.mktime(time.strptime(str(new_start_time), date_format)))

        new_end_time = str(self.request.POST['end_time'])
        new_end_epoch = int(time.mktime(time.strptime(str(new_end_time), date_format)))

        new_car_id = self.request.POST['car_id']

        for BookingCarInfo in bookingcarinfo_list:
            if str(BookingCarInfo.start_time + timedelta(hours=9))[:10] == new_start_day and BookingCarInfo.car_id == new_car_id:

                if int(time.mktime((BookingCarInfo.end_time + timedelta(hours=9)).timetuple())) > new_start_epoch and new_start_epoch >= int(
                        time.mktime((BookingCarInfo.start_time + timedelta(hours=9)).timetuple())):
                    return HttpResponseRedirect('/booking/fail')

                elif new_end_epoch > int(time.mktime((BookingCarInfo.start_time + timedelta(hours=9)).timetuple())) and int(
                        time.mktime((BookingCarInfo.start_time + timedelta(hours=9)).timetuple())) >= new_start_epoch:
                    return HttpResponseRedirect('/booking/fail')

                else:
                    pass

        form.instance.owner = self.request.user
        return super(BookingCarCreateView, self).form_valid(form)


class BookingCarDeleteView(LoginRequiredMixin, DeleteView) :
    model = BookingCarInfo
    template_name = 'bookingcar_confirm_delete.html'
    success_url = reverse_lazy('close')

    def delete(self, request, *args, ** kwargs):
        self.object = self.get_object()
        obj = super(BookingCarDeleteView, self).get_object()

        if obj.owner == self.request.user:

            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect('/car/alert/')

class BookingCarChangeLV(LoginRequiredMixin, ListView):
    template_name = 'bookingcar_change_list.html'

    def get_queryset(self):
        return BookingCarInfo.objects.filter(owner=self.request.user)

class AlertCarView(TemplateView):
    template_name = 'bookingcar_del_alert.html'

class FailCarView(TemplateView):
    template_name = 'bookingcar_fail.html'

class BookingCarUpdateView(LoginRequiredMixin, UpdateView) :
    model = BookingCarInfo
    form_class = CreateCarForm
    template_name = 'bookingcar_form.html'
    success_url = reverse_lazy('close')
