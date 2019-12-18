from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from .forms import LoginForm
from django.shortcuts import render  #ここは何に使う？

class AccountLoginView(LoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"

class AccountIndexView(TemplateView):
    template_name = 'accounts/index.html'
