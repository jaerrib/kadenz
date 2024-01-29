from django.db import models
from django.urls import reverse

from organizations.models import Organization


class Event(models.Model):
    organization = models.ForeignKey(
        Organization,
        related_name="events",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=45)
    description = models.TextField(null=True, blank=True)
    street = models.CharField(max_length=100, null=False, blank=True)
    city = models.CharField(max_length=45, null=False, blank=True)
    state = models.CharField(max_length=45, null=False, blank=True)
    location = models.TextField(null=True, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"pk": self.pk})
