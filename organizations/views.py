from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Organization


class HomePageView(TemplateView):
    template_name = "home.html"


class OrganizationListView(ListView):
    model = Organization
    template_name = "organization_list.html"


class OrganizationDetailView(DetailView):
    model = Organization
    template_name = "organization_detail.html"


class OrganizationCreateView(CreateView):
    model = Organization
    template_name = "organization_new.html"
    fields = ["name", "creator", "details"]


class OrganizationUpdateView(UpdateView):
    model = Organization
    template_name = "organization_edit.html"
    fields = ["name", "details"]


class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = "organization_delete.html"
    success_url = reverse_lazy("organization_list")
