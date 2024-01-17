from django import forms
from django.forms import ModelForm

from .models import Event


class DateInput(forms.DateInput):
    input_type = "date"


class EventCreateForm(ModelForm):
    class Meta:
        model = Event
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
        widgets = {
            "start_date": DateInput(),
            "end_date": DateInput(),
        }


class EventUpdateForm(ModelForm):
    class Meta:
        model = Event
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
        widgets = {
            "start_date": DateInput(),
            "end_date": DateInput(),
        }
