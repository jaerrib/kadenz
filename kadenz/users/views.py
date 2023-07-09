from django.shortcuts import render, HttpResponse, redirect
# from django.contrib.auth.models import User
from .models import User
from organizations.models import Organization
# from django.contrib.auth import authenticate
from django.contrib import messages
import bcrypt


# Create your views here.
def index(request):
    return render(request, "index.html")

def login_process(request):
    # user = authenticate(username=request.POST["username"], password=request.POST["password"])
    # if user is not None:
    #     context = {
    #         "first_name": user.first_name,
    #         "last_name": user.last_name,
    #         "email": user.email,
    #     }
    #     return render(request, "result.html", context)
    # else:
    #     return HttpResponse("placeholder for failed login")

        user = User.objects.filter(email=request.POST['email']) # why are we using filter here instead of get?
        if user: # note that we take advantage of truthiness here: an empty list will return false
            logged_user = user[0]
        # assuming we only have one user with this username, the user would be first in the list we get back
        # of course, we should have some logic to prevent duplicates of usernames when we create users
        # use bcrypt's check_password_hash method, passing the hash from our database and the password from the form
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            # if we get True after checking the password, we may put the user id in session
            request.session['userid'] = logged_user.id
            print(request.session['userid'])
            # never render on a post, always redirect!
            return redirect('/dashboard/')
        # if we didn't find anything in the database by searching by username or if the passwords don't match,
        # redirect back to a safe route
        return redirect("/")

def logout(request):
    request.session.clear()
    return redirect("/")


def registration(request):
    return render(request, "registration.html")

def registration_process(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect("/registration/")
    else:
        password = request.POST["password"]
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
        user = User.objects.create(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            email=request.POST["email"],
            password=pw_hash)
        user.save()
        return redirect("/dashboard/")


def dashboard(request):
    user_organizations = Organization.objects.filter(creator=User.objects.get(id=request.session["userid"]))

    context = {
    	"user_organizations": user_organizations
    }
    return render(request, "dashboard.html", context)
