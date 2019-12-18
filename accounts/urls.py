from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.AccountIndexView.as_view(), name='index'),
    path('login/', views.AccountLoginView.as_view(), name='login'),
]
