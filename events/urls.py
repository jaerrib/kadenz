from django.urls import path

from .views import (
    EventListView,
    EventListReverseView,
    EventDetailView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
)

urlpatterns = [
    path(
        "new/<int:organization_pk>/",
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
    path(
        "reverse/",
        EventListReverseView.as_view(),
        name="event_list_reverse",
    ),
]
