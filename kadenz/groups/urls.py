from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_groups),
    path('<int:group_id>/', views.view_group),
    path('<int:group_id>/edit/', views.edit_group),
    path('<int:group_id>/delete/', views.delete_group),
    path('new/', views.new_group),
]