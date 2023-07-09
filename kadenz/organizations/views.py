from django.shortcuts import render, redirect, HttpResponse
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
from .models import Organization
from django.contrib import messages
from users.models import User

# Create your views here.
# class AllOrganizations(ListView):
#     model = Organization
#     context_object_name = "all_organizations"

# class OrganizationDetail(DetailView):
#     model = Organization
#     context_object_name = "organization"
#     template_name = "organizations/organization.html"

# class OrganizationCreate(CreateView):
#     model = Organization
#     fields = '__all__'
#     success_url = reverse_lazy('all_organizations')

# class OrganizationEdit(UpdateView):
#     model = Organization
#     fields = '__all__'
#     success_url = reverse_lazy('all_organizations')

# class OrganizationDelete(DeleteView):
#     model = Organization
#     context_object_name = "organization"
#     success_url = reverse_lazy('all_organizations')


def all_organizations(request):
    context = {
    	"all_organizations": Organization.objects.all()
    }
    return render(request, "organization_list.html", context)

def view_organization(request, organization_id):
    context = {
    	"organization": Organization.objects.get(id=organization_id)
    }
    return render(request, "organization.html", context)

def edit_organization(request, organization_id):
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


# def edit_organization_process(request, organization_id):
#     organization = Organization.objects.get(id=organization_id)
#     organization.name = request.POST["name"]
#     organization.details = request.POST["details"]
#     organization.save()
#     return redirect(f"/{organization.id}/")

def delete_organization(request, organization_id):
    organization = Organization.objects.get(id=organization_id)
    organization.delete()
    return redirect("/organizations")

def new_organization(request):
    return render(request, "new-organization.html")

def new_organization_process(request):
    creator = User.objects.get(id=1) # will need to change to the logged in user
    organization = Organization(
        name=request.POST["name"],
        details=request.POST["details"],
        creator=creator
    )
    errors = Organization.objects.basic_validator(request.POST)
    if len(errors) > 0:
    # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
            return redirect('/organizations/new')
        else:
            organization.save()
            return redirect("/organizations/")

def edit_organization_process(request, organization_id):
    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = Organization.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'/organizations/{organization_id}/edit')
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the blog to be updated, make the changes, and save
        organization = Organization.objects.get(id=organization_id)
        organization.name = request.POST["name"]
        organization.details = request.POST["details"]
        organization.save()
        messages.success(request, "Organizations successfully updated")
        # redirect to a success route
        return redirect(f"/{organization.id}/")

