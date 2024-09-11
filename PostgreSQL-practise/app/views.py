from django.shortcuts import render
from .models import Student 
# Create your views here.
def index(request):

    #Create object for student module
    obj=Student.objects.all()
    context={
        "obj":obj,
    }

    #We simply return a template
    return render(request, "index.html", context); 

