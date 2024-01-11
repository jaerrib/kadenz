from django.urls import path

from .views import (
    EventListView,
    EventDetailView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
)

urlpatterns = [
    path(
        "new/",
        EventCreateView.as_view(),
        name="event_new",
    ),
    path(
        "<int:pk>/",
        EventDetailView.as_view(),
        name="event_detail",
    ),
    path(
        "<int:pk>/edit/",
        EventUpdateView.as_view(),
        name="event_edit",
    ),
    path(
        "<int:pk>/delete/",
        EventDeleteView.as_view(),
        name="event_delete",
    ),
    path(
        "",
        EventListView.as_view(),
        name="event_list",
    ),
]
