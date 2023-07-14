from django.db import models
from organizations.models import Organization
from users.models import User

# Create your models here.
class EventManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["name"]) < 5:
            errors["name"] = "Event name should be at least 5 characters"
        if len(postData["description"]) < 10:
            errors["description"] = "Description should be at least 10 characters"
        if postData["street"] == "":
            errors["street"] = "Street address is required"
        if postData["city"] == "":
            errors["city"] = "City is required"
        if postData["state"] == "":
            errors["state"] = "State is required"
        if postData["start_date"] == "":
            errors["start_date"] = "Start date is required"
        if postData["end_date"] == "":
            errors["end_date"] = "End date is required"
        return errors

class Event(models.Model):
    organization = models.ForeignKey(Organization, related_name="events", on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    description = models.TextField(null=True, blank=True)
    street = models.CharField(max_length=100, null=False, blank=True)
    city = models.CharField(max_length=45, null=False, blank=True)
    state = models.CharField(max_length=45, null=False, blank=True)
    location = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=False, blank=True)
    end_date = models.DateField(null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User)
    objects = EventManager()

    def __str__(self):
        return self.name