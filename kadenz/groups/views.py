from django.shortcuts import render, HttpResponse

# Create your views here.
def all_groups(request):
    return HttpResponse("placeholder for viewing all groups")

def view_group(request, group_id):
    return HttpResponse(f"placeholder to display group number: {group_id}")

def edit_group(request, group_id):
    return HttpResponse(f"placeholder to edit group number: {group_id}")

def delete_group(request, group_id):
    return HttpResponse(f"placeholder to delete group number: {group_id}")

def new_group(request):
    return HttpResponse("placeholder for displaying new group page")
