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

#Import User model
from .models import User

#For access to time
from django.utils import timezone

# Create your views here.
# request -> response
# request handler
# action

def mainPageView(request):
    print("In mainPageView")
    #return main page  
    # 
    #Now we use html in templates  
    return render(request, 'mainPage.html', {'user': request.user}) 

def successPageView(request):
    print("In successPageView")

    return render(request, 'dashboardPage.html')

#For registering a user
def registerPageView(request):
    print("In registerPageView")

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
            if User.objects.filter(email=email1).exists():
                messages.info(request, 'Email is already registered with this site')

                return redirect('registerPage')
            else:

                #Hash the password
                hashedPwd=make_password(password)

                #Create an instance of a model
                user=User(
                    username=username1,
                    email=email1,
                    password=hashedPwd,
                    name=name1)
                
                #Instance of a model saved to database
                user.save()

                #Uncomment me plz
                #Automatically log user in
                login(request, user)
                #Update user object to last logged in as now
                user.last_logged_in = timezone.now()
                user.save()
                messages.success(request, "Successful registration")
                
                return redirect('dashboardPage')
        else:
            print(f"password={password}")
            print(f"password1={password1}")
            messages.info(request, 'Passwords are not the same')
            return redirect('registerPage')

    return render(request, 'registerPage.html')

def loginPageView(request):
    print("In loginPageView")
    
    #We do not log in an already logged in user
    if request.user.is_authenticated:
        return redirect(mainPageView)

    if request.method == 'POST':
        inputUsername = request.POST.get('username')
        inputPassword = request.POST.get('password')
        
        user = authenticate(request, username=inputUsername,
                            password=inputPassword)
    
        print(f"User is: {user}")

        if user:
            #Update user object to last logged in as now
            user.last_logged_in = timezone.now()

            #Save this
            user.save()

            #log the user in
            login(request, user)
            
            messages.info(request, 'Successful log in!')
            return redirect('dashboardPage')
        else:
            messages.info(request, 'Unsuccessful log in')
            return redirect('loginPage')

    return render(request, 'loginPage.html')

#For logging out
def logoutPageView(request):
    print("In logoutPageView")

    #If user is not authenticated, redirect to log in
    if request.user.is_authenticated != True:
        return redirect(loginPageView)

    logout(request)

    messages.info(request, 'Successfully logged out!')

    return redirect('mainPage')

#Dashboard for logged in users
def dashboardPageView(request):
    print("In dashboardPageView")

    return render(request, 'dashboardPage.html')

def nonsuperuserPageView(request):
    return render(request, 'nonsuperuserPage.html')

def contactusPageView(request):

    if request.method=='POST':
        print("Form entered!")
        
        #Find the type of form this is
        formType = request.POST.get('formType')
        if formType == "Send message":
            
            messages.info(request, 'Successfully sent message!')

            return redirect('contactusPage')


    return render(request, 'contactusPage.html')