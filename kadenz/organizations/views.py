from django.shortcuts import render, HttpResponse

# Create your views here.
def all_organizations(request):
    return HttpResponse("placeholder for viewing all organizations")

def view_organization(request, organization_id):
    return HttpResponse(f"placeholder to display organization number: {organization_id}")

def edit_organization(request, organization_id):
    return HttpResponse(f"placeholder to edit organization number: {organization_id}")

def delete_organization(request, organization_id):
    return HttpResponse(f"placeholder to delete organization number: {organization_id}")

def new_organization(request):
    return render(request, "new-organization.html")
