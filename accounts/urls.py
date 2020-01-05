from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.AccountIndexView.as_view(), name='index'),
    path('login/', views.AccountLoginView.as_view(), name='login'),
    path('signup/', views.AccountCreateView.as_view(), name='signup'),
    path('detail/<str:username>/', views.AccountDetail.as_view(), name='detail'),
    path('edit/<str:username>/', views.AccountEdit.as_view(), name='edit'),
]
