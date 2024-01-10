from django.db import models
from django.urls import reverse


class Organization(models.Model):
    name = models.CharField(max_length=45)
    creator = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    details = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("organization_detail", kwargs={"pk": self.pk})
