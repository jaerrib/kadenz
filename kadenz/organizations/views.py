from django.shortcuts import render, redirect, HttpResponse
from .models import Organization
from events.models import Event
from django.contrib import messages
from users.models import User

def all_organizations(request):
    if "userid" not in request.session:
        return redirect("/")
    context = {
    	"all_organizations": Organization.objects.all()
    }
    return render(request, "organization_list.html", context)

def view_organization(request, organization_id):
    if "userid" not in request.session:
        return redirect("/")
    context = {
    	"organization": Organization.objects.get(id=organization_id),
        "all_events": Event.objects.filter(organization=organization_id),
    }
    return render(request, "organization.html", context)

def edit_organization(request, organization_id):
    if "userid" not in request.session:
        return redirect("/")
    organization = Organization.objects.get(id=organization_id)
    context = {
        "organization": {
            "id": organization.id,
            "name": organization.name,
            "details": organization.details,
            "created_at": organization.created_at,
            "updated_at": organization.updated_at,
        }
    }
    return render(request, "edit.html", context)


def delete_organization(request, organization_id):
    if "userid" not in request.session:
        return redirect("/")
    organization = Organization.objects.get(id=organization_id)
    organization.delete()
    return redirect("/organizations")


def new_organization(request):
    if "userid" not in request.session:
        return redirect("/")
    return render(request, "new-organization.html")


def new_organization_process(request):
    if "userid" not in request.session:
        return redirect("/")
    creator = User.objects.get(id=request.session["userid"])
    organization = Organization(
        name=request.POST["name"],
        details=request.POST["details"],
        creator=User.objects.get(id=request.session["userid"])
    )
    errors = Organization.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/organizations/new')
    else:
        organization.save()
        return redirect("/dashboard/")


def edit_organization_process(request, organization_id):
    if "userid" not in request.session:
        return redirect("/")
    errors = Organization.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/organizations/{organization_id}/edit')
    else:
        organization = Organization.objects.get(id=organization_id)
        organization.name = request.POST["name"]
        organization.details = request.POST["details"]
        organization.save()
        messages.success(request, "Organizations successfully updated")
        return redirect(f"/{organization.id}/")
