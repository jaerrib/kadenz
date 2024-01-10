from django.urls import path

from .views import HomePageView, OrganizationListView, OrganizationDetailView

urlpatterns = [
    path("organizations/", OrganizationListView.as_view(),
         name="organization_list"),
    path(
        "organizations/<int:pk>/",
        OrganizationDetailView.as_view(),
        name="organization_detail",
    ),
    path("", HomePageView.as_view(), name="home"),
]
