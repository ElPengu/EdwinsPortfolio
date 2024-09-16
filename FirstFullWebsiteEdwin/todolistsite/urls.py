from django.urls import path, include

from . import views
#We can reference view function

#Spell properly
urlpatterns = [
    path('', views.todolistPageView, name='todolistPage'),
    
]