from django.urls import path

from .views import (
    HomePageView,
    OrganizationListView,
    OrganizationDetailView,
    OrganizationCreateView,
    OrganizationUpdateView,
    OrganizationDeleteView,
)

urlpatterns = [
    path(
        "organizations/new/",
        OrganizationCreateView.as_view(),
        name="organization_new",
    ),
    path(
        "organizations/<int:pk>/",
        OrganizationDetailView.as_view(),
        name="organization_detail",
    ),
    path(
        "organizations/<int:pk>/edit/",
        OrganizationUpdateView.as_view(),
        name="organization_edit",
    ),
    path(
        "organizations/<int:pk>/delete/",
        OrganizationDeleteView.as_view(),
        name="organization_delete",
    ),
    path("organizations/", OrganizationListView.as_view(),
         name="organization_list"),
    path("", HomePageView.as_view(), name="home"),
]
