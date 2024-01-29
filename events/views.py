from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from organizations.models import Organization
from .forms import EventCreateForm, EventUpdateForm
from .models import Event


class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = "event_list.html"


class EventListReverseView(LoginRequiredMixin, ListView):
    model = Event
    template_name = "event_list.html"

    queryset = Event.objects.order_by("-pk")
    context_object_name = "event_list"


class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = "event_detail.html"


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_template = EventCreateForm
    template_name = "event_new.html"
    fields = [
        "name",
        "organization",
        "description",
        "street",
        "city",
        "state",
        "start_date",
        "end_date",
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = EventCreateForm()
        context["organization"] = Organization.objects.get(
            pk=self.kwargs["organization_pk"]
        )
        return context

    def form_valid(self, form):
        form.instance.organization = Organization.objects.get(
            pk=self.kwargs["organization_pk"]
        )
        form.instance.creator = self.request.user
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    form_template = EventUpdateForm
    template_name = "event_edit.html"
    fields = [
        "name",
        "description",
        "street",
        "city",
        "state",
        "start_date",
        "end_date",
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = EventUpdateForm()
        return context

    def test_func(self):
        obj = self.get_object()
        return obj.creator == self.request.user


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = "event_delete.html"
    success_url = reverse_lazy("event_list")

    def test_func(self):
        obj = self.get_object()
        return obj.creator == self.request.user
