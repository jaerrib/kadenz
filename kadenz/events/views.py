from django.shortcuts import render, HttpResponse, redirect
from . models import Event
from organizations.models import Organization
from datetime import date

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

    # string_input_with_date = str(event.start_date)
    # print(string_input_with_date)
    # start_date = (string_input_with_date, "%M/%d/%Y")


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
    return render(request, "edit-event.html", context)


def new_event_process(request):
    errors = Event.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/organizations/new')
    else:
        event = Event(
            name=request.POST["name"],
            description=request.POST["description"],
            location=request.POST["location"],
            start_date=request.POST["start_date"],
            end_date=request.POST["end_date"],
            organization=Organization.objects.get(id=request.POST['organization_id'])
        )
        event.save()
        return redirect("/organizations/")


def edit_event_process(request):
    errors = Event.ojects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/events/{event.event_id}/edit')
    else:
        # event = Event.objects.get(id=event_id)
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
    organization = Organization.objects.get(id=organization_id)
    context = {"organization": organization}
    return render(request, "new-event.html", context)


def rsvp(request, event_id):
    return HttpResponse(f"placeholder to rsvp to event number {event_id}")
