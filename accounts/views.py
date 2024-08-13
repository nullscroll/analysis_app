from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth import logout
from django.http import HttpRequest
from django.shortcuts import render

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class LogOutView(TemplateView):
    template_name = "registration/logout.html"

    def get(self, request: HttpRequest):
        logout(request)
        return render(request, self.template_name)
