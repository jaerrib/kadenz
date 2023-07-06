from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_events),
    path('<int:event_id>/', views.view_event),
    path('<int:event_id>/edit/', views.edit_event),
    path('<int:event_id>/delete/', views.delete_event),
    path('new/<int:group_id>', views.new_event),
    path('<int:event_id>/rsvp/', views.rsvp),
]