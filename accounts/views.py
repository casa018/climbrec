from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, CreateView
from .forms import LoginForm, CreateForm
from django.urls import reverse_lazy
from django.shortcuts import render  #ここは何に使う？

class AccountLoginView(LoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"

class AccountCreateView(CreateView):
    form_class = CreateForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("login")

class AccountIndexView(TemplateView):
    template_name = 'accounts/index.html'
