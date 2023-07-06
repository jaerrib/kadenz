from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def login_process(request):
    return HttpResponse("placeholder for processing login form data")

def registration(request):
    return HttpResponse("placeholder for displaying registration page")

def registration_process(request):
    return HttpResponse("placeholder for processing registration form data")

def dashboard(request):
    return HttpResponse("placeholder for displaying dashboard page")
