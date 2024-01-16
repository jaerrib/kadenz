from django.contrib import admin

from events.models import Event
from .models import Organization


class EventInLine(admin.TabularInline):
    model = Event
    extra = 0


class OrganizationAdmin(admin.ModelAdmin):
    inlines = [
        EventInLine,
    ]
    list_display = (
        "name",
        "creator",
        "details",
    )


admin.site.register(Organization, OrganizationAdmin)
