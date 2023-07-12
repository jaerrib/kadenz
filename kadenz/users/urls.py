from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/process/', views.login_process),
    path('registration/', views.registration),
    path('registration/process/', views.registration_process),
    path('dashboard/', views.dashboard),
    path('logout/', views.logout),
]
