from django.shortcuts import render

from django.http import HttpResponse
# We can
# Pull data from db
#Transform data
#Send email

# Create your views here.
# request -> response
# request handler
# action

def say_hello(request):
    #return HttpResponse('Hello World')  
    # 
    #Now we use html in templates  
    return render(request, 'hello.html', {'name': 'Edwin'}) 

def cssPlayground(request):

    return render(request, 'cssPlayground.html')