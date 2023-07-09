from django.db import models
from users.models import User

# Create your models here.
class OrganizationManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["name"]) < 5:
            errors["name"] = "Organization name should be at least 5 characters"
        if len(postData["details"]) < 10:
            errors["details"] = "Details should be at least 10 characters"
        return errors

class Organization(models.Model):
    creator = models.ForeignKey(User, related_name="organizations", on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    details = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = OrganizationManager()

    def __str__(self):
        return self.name
