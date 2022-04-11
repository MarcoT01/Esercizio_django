# from django.http import HttpResponse
#
#
# def home(request):
# return HttpResponse("Hello, World!")
from datetime import datetime

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView


def home(request):
    return render(request, "home.html")


def privacy(request):
    return render(request, "privacy.html", context={'year': datetime.now().year})


class UserCreateView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "User_create.html"
    success_url = reverse_lazy("home_page")


class UserLoginView(LoginView):
    template_name = "il_mio_template"
