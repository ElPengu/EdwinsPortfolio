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

#Import to-do list item model
from .models import todoListItem

#For access to time
from django.utils import timezone

# Create your views here.
# request -> response
# request handler
# action

def todolistPageView(request):
    print("In to do list Page View")

    #To access user attributes
    user = request.user

    #If we read a POST
    if request.method=='POST':
        title1 = request.POST.get('title')
        description1 = request.POST.get('description')

        #We can only add items with a non-empty title
        #Description may be non-empty
        if title1 == None or len(title1) == 0:
            messages.info(request, 'Failed to add to-do list item. The title must not be empty')
        else:
            #Create instance of a model
            todolistItem = todoListItem(
                user_id=user,
                title=title1,
                description=description1
            )

            #Save this instance of the model
            todolistItem.save()
            
            messages.info(request, 'To-do list item added!')

        return redirect('todolistPage')

    #Now we use html in templates  
    #Pass the to-do list items too
    return render(request, 'todolistPage.html', {'todolistItemInstances': todoListItem.objects.filter(user_id=user)}) 