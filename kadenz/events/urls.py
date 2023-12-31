from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_events),
    path('reverse', views.all_events_reverse),
    path('<int:event_id>/', views.view_event),
    path('<int:event_id>/edit/', views.edit_event),
    path('edit/process/', views.edit_event_process),
    path('<int:event_id>/delete/', views.delete_event),
    path('new/<int:organization_id>/', views.new_event),
    path('new/process/', views.new_event_process),
    path('<int:event_id>/rsvp/', views.rsvp),
    path('<int:event_id>/rsvp/cancel/', views.rsvp_cancel),
]
