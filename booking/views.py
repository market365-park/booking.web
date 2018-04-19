# -*- encoding: utf-8 -*-
from booking.forms import PostSearchForm, CreateForm
from booking.models import BookingInfo

from datetime import datetime, timedelta, time
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.http.response import *
from MRBS.views import LoginRequiredMixin

import datetime, time

class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'booking_search.html'

    def form_valid(self, form) :
        schWord = '%s' % self.request.POST['search_word']
        post_list = BookingInfo.objects.filter(Q(title__icontains=schWord) | Q(description__icontains=schWord) | Q(content__icontains=schWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)


class BookingCreateView(LoginRequiredMixin, CreateView, ListView):
    model = BookingInfo
    form_class = CreateForm
    template_name = 'booking_form.html'
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
                'room_id': self.request.GET.get("room")
            }

    def form_valid(self, form):
        bookinginfo_list = self.model.objects.all()
        date_format = '%Y-%m-%d %H:%M'

        new_start_time = str(self.request.POST['start_time'])
        new_start_day = new_start_time[:10]
        new_start_epoch = int(time.mktime(time.strptime(str(new_start_time), date_format)))

        new_end_time = str(self.request.POST['end_time'])
        new_end_epoch = int(time.mktime(time.strptime(str(new_end_time), date_format)))

        new_room_id = self.request.POST['room_id']

        for BookingInfo in bookinginfo_list:
            if str(BookingInfo.start_time + timedelta(hours=9))[:10] == new_start_day and BookingInfo.room_id == new_room_id:

                if int(time.mktime((BookingInfo.end_time + timedelta(hours=9)).timetuple())) > new_start_epoch and new_start_epoch >= int(
                        time.mktime((BookingInfo.start_time + timedelta(hours=9)).timetuple())):
                    return HttpResponseRedirect('/booking/fail')

                elif new_end_epoch > int(time.mktime((BookingInfo.start_time + timedelta(hours=9)).timetuple())) and int(
                        time.mktime((BookingInfo.start_time + timedelta(hours=9)).timetuple())) >= new_start_epoch:
                    return HttpResponseRedirect('/booking/fail')

                else:
                    pass


        form.instance.owner = self.request.user
        return super(BookingCreateView, self).form_valid(form)


class BookingDeleteView(LoginRequiredMixin, DeleteView) :
    model = BookingInfo
    template_name = 'booking_confirm_delete.html'
    success_url = reverse_lazy('close')

    def delete(self, request, *args, ** kwargs):
        self.object = self.get_object()
        obj = super(BookingDeleteView, self).get_object()

        if obj.owner == self.request.user:

            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect('/booking/alert/')

class BookingChangeLV(LoginRequiredMixin, ListView):
    template_name = 'booking_change_list.html'

    def get_queryset(self):
        return BookingInfo.objects.filter(owner=self.request.user)

class AlertView(TemplateView):
    template_name = 'booking_del_alert.html'

class FailView(TemplateView):
    template_name = 'booking_fail.html'

class BookingUpdateView(LoginRequiredMixin, UpdateView) :
    model = BookingInfo
    form_class = CreateForm
    template_name = 'booking_form.html'
    success_url = reverse_lazy('close')
