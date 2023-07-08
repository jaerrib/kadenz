from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_organizations),
    path('<int:organization_id>/', views.view_organization),
    path('<int:organization_id>/edit/', views.edit_organization),
    path('<int:organization_id>/delete/', views.delete_organization),
    path('new/', views.new_organization),
]