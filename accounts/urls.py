from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.AccountIndexView.as_view(), name='index'),
    path('login/', views.AccountLoginView.as_view(), name='login'),
    path('signup/', views.AccountCreateView.as_view(), name='signup'),
    path('detail/<str:username>/', views.AccountDetail.as_view(), name='detail'),
    path('edit/<str:username>/', views.AccountEdit.as_view(), name='edit'),
    path('passwordchange/', views.AccountPasswordChangeView.as_view(),
         name='passwordchange'),
    path('passwordchangedone/', views.AccountPasswordChangeDoneView.as_view(),
         name='passwordchangedone'),
    path('delete/<str:username>/', views.AccountDeleteView.as_view(), name='delete'),
    path('passwordreset/', views.AccountPasswordResetView.as_view(),
         name='passwordreset'),
    path('passwordreset/done/', views.AccountPasswordResetDoneView.as_view(),
         name='passwordresetdone'),
    path('passwordreset/confirm/<uidb64>/<token>/',
         views.AccountPasswordConfirmView.as_view(), name='passwordresetconfirm'),
    path('passwordreset/complete/', views.AccountPassrowdResetCompleteView.as_view(),
         name='passwordresetcomplete'),
]
