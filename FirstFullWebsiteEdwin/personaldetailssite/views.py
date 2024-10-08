from django.shortcuts import render

from django.http import HttpResponse
# We can
# Pull data from db
#Transform data
#Send email

#For logging in and registering
from django.contrib.auth.models import User,auth
#Above gets model!
from django.shortcuts import redirect
from django.contrib import messages
#To hash passwords
from django.contrib.auth.hashers import make_password

#For logging users in or out
from django.contrib.auth import authenticate, login, logout

#For access to time
from django.utils import timezone

# Create your views here.
# request -> response
# request handler
# action

def personaldetailsPageView(request):

    return render(request, 'personaldetailsPage.html')