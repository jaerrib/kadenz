from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Organization(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    organization_name = models.CharField(max_length=45)
    details = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.organization_name
