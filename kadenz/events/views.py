from .models import Event
from django.contrib import messages
from django.shortcuts import render, redirect
from organizations.models import Organization
from users.models import User
import os
import requests


# Create your views here.
def all_events(request):
    if "userid" not in request.session:
        return redirect("/")
    context = {
        "all_events": Event.objects.all().order_by('start_date')
    }
    return render(request, "event-list.html", context)


def all_events_reverse(request):
    if "userid" not in request.session:
        return redirect("/")
    context = {
        "all_events": Event.objects.all().order_by('-start_date')
    }
    return render(request, "event-list.html", context)


def view_event(request, event_id):
    if "userid" not in request.session:
        return redirect("/")
    event = Event.objects.get(id=event_id)
    status = False
    if event.users.count() != 0:
        for user in event.users.all():
            if user.id == request.session["userid"]:
                status = True
    context = {
        "event": event,
        "status": status
    }
    return render(request, "event.html", context)


def edit_event(request, event_id):
    if "userid" not in request.session:
        return redirect("/")
    event = Event.objects.get(id=event_id)
    context = {
        "event": {
            "id": event.id,
            "organization": event.organization,
            "name": event.name,
            "description": event.description,
            "street": event.street,
            "city": event.city,
            "state": event.state,
            "start_date": event.start_date,
            "end_date": event.end_date,
            "created_at": event.created_at,
            "updated_at": event.updated_at,
        }
    }
    return render(request, "edit-event.html", context)


def new_event_process(request):
    if "userid" not in request.session:
        return redirect("/")
    errors = Event.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        organization_id = request.POST["organization_id"]
        return redirect(f'/events/new/{organization_id}')
    else:
        event = Event(
            name=request.POST["name"],
            description=request.POST["description"],
            street=request.POST["street"],
            city=request.POST["city"],
            state=request.POST["state"],
            start_date=request.POST["start_date"],
            end_date=request.POST["end_date"],
            organization=Organization.objects.get(id=request.POST['organization_id'])
        )
        event.save()
        lookup = f"{event.street} {event.city} {event.state}"
        headers = os.environ.get("KEY")
        response = requests.get(f"https://api.tomtom.com/search/2/geocode/{lookup}.json?storeResult=false&view=Unified&key={headers}")
        lon = response.json()['results'][0]['position']['lon']
        lat = response.json()['results'][0]['position']['lat']
        event.location = f"https://api.tomtom.com/map/1/staticimage?key={headers}&zoom=15&center={lon},{lat}&format=png&layer=basic&style=main&width=512&height=512&view=Unified&language=en-US"
        event.save()
        return redirect(f"/events/{event.id}/")


def edit_event_process(request):
    if "userid" not in request.session:
        return redirect("/")
    errors = Event.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        event_id = request.POST["event_id"]
        return redirect(f'/events/{event_id}/edit')
    else:
        event = Event.objects.get(id=request.POST["event_id"])
        event.name = request.POST["name"]
        event.description = request.POST["description"]
        event.street = request.POST["street"]
        event.city = request.POST["city"]
        event.state = request.POST["state"]
        event.start_date = request.POST["start_date"]
        event.end_date = request.POST["end_date"]
        event.save()
        lookup = f"{event.street} {event.city} {event.state}"
        headers = os.environ.get("KEY")
        response = requests.get(f"https://api.tomtom.com/search/2/geocode/{lookup}.json?storeResult=false&view=Unified&key={headers}")
        lon = response.json()['results'][0]['position']['lon']
        lat = response.json()['results'][0]['position']['lat']
        event.location = f"https://api.tomtom.com/map/1/staticimage?key={headers}&zoom=15&center={lon},{lat}&format=png&layer=basic&style=main&width=512&height=512&view=Unified&language=en-US"
        event.save()
        messages.success(request, "Event successfully updated")
        return redirect(f"/events/{event.id}/")


def delete_event(request, event_id):
    if "userid" not in request.session:
        return redirect("/")
    event = Event.objects.get(id=event_id)
    event.delete()
    return redirect("/dashboard/")


def new_event(request, organization_id):
    if "userid" not in request.session:
        return redirect("/")
    organization = Organization.objects.get(id=organization_id)
    context = {"organization": organization}
    return render(request, "new-event.html", context)


def rsvp(request, event_id):
    if "userid" not in request.session:
        return redirect("/")
    event = Event.objects.get(id=event_id)
    user = User.objects.get(id=request.session["userid"])
    event.users.add(user)
    return redirect(f"/events/{event.id}/")


def rsvp_cancel(request, event_id):
    if "userid" not in request.session:
        return redirect("/")
    event = Event.objects.get(id=event_id)
    user = User.objects.get(id=request.session["userid"])
    event.users.remove(user)
    return redirect(f"/events/{event.id}/")
