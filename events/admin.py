from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = (
        "organization",
        # "creator",
        "name",
        "description",
        "street",
        "city",
        "state",
        "start_date",
        "end_date",
    )


admin.site.register(Event, EventAdmin)
