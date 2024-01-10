from django.views.generic import TemplateView, ListView, DetailView

from .models import Organization


class HomePageView(TemplateView):
    template_name = "home.html"


class OrganizationListView(ListView):
    model = Organization
    template_name = "organization_list.html"


class OrganizationDetailView(DetailView):
    model = Organization
    template_name = "organization_detail.html"
