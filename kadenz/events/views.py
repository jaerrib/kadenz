from django.shortcuts import render, HttpResponse

# Create your views here.
def all_events(request):
    return HttpResponse("placeholder for viewing all events")

def view_event(request, event_id):
    return HttpResponse(f"placeholder to display event number: {event_id}")

def edit_event(request, event_id):
    return HttpResponse(f"placeholder to edit event number: {event_id}")

def delete_event(request, event_id):
    return HttpResponse(f"placeholder to delete event number: {event_id}")

def new_event(request, organization_id):
    return HttpResponse(f"placeholder for creating new event for group number; {organization_id}")

def rsvp(request, event_id):
    return HttpResponse(f"placeholder to rsvp to event number {event_id}")
