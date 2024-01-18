from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Organization


class HomePageView(TemplateView):
    template_name = "home.html"


class OrganizationListView(LoginRequiredMixin, ListView):
    model = Organization
    template_name = "organization_list.html"

    queryset = Organization.objects.order_by("name")
    context_object_name = "organization_list"


class OrganizationListReverseView(LoginRequiredMixin, ListView):
    model = Organization
    template_name = "organization_list.html"

    queryset = Organization.objects.order_by("-name")
    context_object_name = "organization_list"


class OrganizationDetailView(LoginRequiredMixin, DetailView):
    model = Organization
    template_name = "organization_detail.html"


class OrganizationCreateView(LoginRequiredMixin, CreateView):
    model = Organization
    template_name = "organization_new.html"
    fields = ["name", "details"]

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class OrganizationUpdateView(LoginRequiredMixin, UserPassesTestMixin,
                             UpdateView):
    model = Organization
    template_name = "organization_edit.html"
    fields = ["name", "details"]

    def test_func(self):
        obj = self.get_object()
        return obj.creator == self.request.user


class OrganizationDeleteView(LoginRequiredMixin, UserPassesTestMixin,
                             DeleteView):
    model = Organization
    template_name = "organization_delete.html"
    success_url = reverse_lazy("organization_list")

    def test_func(self):
        obj = self.get_object()
        return obj.creator == self.request.user


class DashboardView(LoginRequiredMixin, ListView):
    model = Organization
    template_name = "dashboard.html"

    def get_queryset(self):
        return Organization.objects.filter(creator=self.request.user.pk)
