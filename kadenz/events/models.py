from django.db import models
from organizations.models import Organization

# Create your models here.
class EventManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # if len(postData["name"]) < 5:
        #     errors["name"] = "Organization name should be at least 5 characters"
        # if len(postData["details"]) < 10:
        #     errors["details"] = "Details should be at least 10 characters"
        return errors

class Event(models.Model):
    organization = models.ForeignKey(Organization, related_name="events", on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    description = models.TextField(null=True, blank=True)
    location = models.TextField(null=False, blank=False)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = EventManager()

    def __str__(self):
        return self.name