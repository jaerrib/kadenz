from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/process/', views.login_process),
    path('registration/', views.registration),
    path('dashboard/', views.dashboard),
]