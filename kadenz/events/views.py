from django.shortcuts import render, HttpResponse, redirect
from . models import Event

# Create your views here.
def all_events(request):
    context = {
    	"all_events": Event.objects.all()
    }
    return render(request, "event_list.html", context)

def view_event(request, event_id):
    context = {
    	"event": Event.objects.get(id=event_id)
    }
    return render(request, "event.html", context)

def edit_event(request, event_id):
    event = Event.objects.get(id=event_id)
    context = {
        "event": {
            "id": event.id,
            "organization": event.organization,
            "name": event.name,
            "description": event.description,
            "location": event.location,
            "start_date": event.start_date,
            "end_date": event.end_date,
            "created_at": event.created_at,
            "updated_at": event.updated_at,
        }
    }
    return render(request, "edit.html", context)

def edit_event_process(request, event_id):
    errors = Event.ojects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/events/{event.event_id}/edit')
    else:
        event = Event.objects.get(id=event_id)
        event.name = request.POST["name"]
        event.description = request.POST["description"]
        event.location = request.POST["location"]
        event.start_date = request.POST["start_date"]
        event.end_date = request.POST["end_date"]
        event.save()
        messages.success(request, "Event successfully updated")
        return redirect(f"/{event.id}/")


def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    return redirect("/dashboard")

def new_event(request, organization_id):
    return HttpResponse(f"placeholder for creating new event for group number; {organization_id}")

def rsvp(request, event_id):
    return HttpResponse(f"placeholder to rsvp to event number {event_id}")
