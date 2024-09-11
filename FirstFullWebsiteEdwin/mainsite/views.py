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

#Import User model
from .models import User as CustomUser

# Create your views here.
# request -> response
# request handler
# action

def mainPageView(request):
    print("HEYY")
    #return main page  
    # 
    #Now we use html in templates  
    return render(request, 'mainPage.html') 

def successPageView(request):

    return render(request, 'successPage.html')

#For registering a user
def registerPageView(request):
    #When we call this function, we will read a 
    #form

    #If we read a POST
    if request.method=='POST':
        username1 = request.POST.get('username')
        email1 = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        name1 = request.POST.get('name')

        if password == password1:
            if CustomUser.objects.filter(email=email1).exists():
                messages.info(request, 'Email is already registered with this site')

                return redirect('registerPage')
            else:

                #Hash the password
                hashedPwd=make_password(password)

                #Create an instance of a model
                user=CustomUser(
                    username=username1,
                    email=email1,
                    password=hashedPwd,
                    name=name1)
                
                #Instance of a model saved to database
                user.save()

                messages.success(request, "Successful registration")
                print("We are here")
                return redirect('successPage')
        else:
            print("HEY")
            print(f"password={password}")
            print(f"password1={password1}")
            messages.info(request, 'Passwords are not the same')
            return redirect('registerPage')

    return render(request, 'registerPage.html')
