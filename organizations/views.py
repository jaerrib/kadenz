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
    fields = ["name", "details"]

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class OrganizationUpdateView(UpdateView):
    model = Organization
    template_name = "organization_edit.html"
    fields = ["name", "details"]


class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = "organization_delete.html"
    success_url = reverse_lazy("organization_list")


class DashboardView(ListView):
    model = Organization
    template_name = "dashboard.html"

    def get_queryset(self):
        return Organization.objects.filter(creator=self.request.user.pk)
