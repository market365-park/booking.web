from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView

from booking.forms import RegisterForm, ProfileUpdateForm
from booking.models import *

from blog.models import *

from car.models import BookingCarInfo, Car

import random

# def check(request):
#     if request.user.is_authenticated():
#         return HttpResponseRedirect('/home/')
#     else:
#         return login(request)

#--- @login_required
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class HomeView(LoginRequiredMixin, ListView):
    context_object_name = 'bookinginfos'
    template_name = 'home.html'
    queryset = BookingInfo.objects.all()


    def get_context_data(self, **kwargs):
            index = Post.objects.filter().count()
            if index != 0 :
                ran_pick = random.randrange(1, index + 1)
                context = super(HomeView, self).get_context_data(**kwargs)
                context['rooms'] = Room.objects.all()
                context['posts'] = Post.objects.all()[ran_pick - 1]
                # And so on for more models
                return context
            else :
                ran_pick = 1
                context = super(HomeView, self).get_context_data(**kwargs)
                context['rooms'] = Room.objects.all()
            # And so on for more models
                return context

class CarHomeView(LoginRequiredMixin, ListView):
    context_object_name = 'bookingcarinfos'
    template_name = 'carhome.html'
    queryset = BookingCarInfo.objects.all()

    def get_context_data(self, **kwargs):
            index = Post.objects.filter().count()
            if index != 0 :
                ran_pick = random.randrange(1, index + 1)
                context = super(CarHomeView, self).get_context_data(**kwargs)
                context['cars'] = Car.objects.all()
                context['posts'] = Post.objects.all()[ran_pick - 1]
                # And so on for more models
                return context
            else :
                ran_pick = 1
                context = super(CarHomeView, self).get_context_data(**kwargs)
                context['cars'] = Car.objects.all()
            # And so on for more models
                return context



class CloseView(TemplateView):
    template_name = 'close.html'

#--- User Creation
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    # model = User
    # queryset = User
    form_class = ProfileUpdateForm
    template_name = 'registration/profile_update.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        users = User.objects.all()
        return users