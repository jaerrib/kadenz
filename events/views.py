from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Event


class EventListView(ListView):
    model = Event
    template_name = "event_list.html"


class EventDetailView(DetailView):
    model = Event
    template_name = "event_detail.html"


class EventCreateView(CreateView):
    model = Event
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

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class EventUpdateView(UpdateView):
    model = Event
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


class EventDeleteView(DeleteView):
    model = Event
    template_name = "event_delete.html"
    success_url = reverse_lazy("event_list")
