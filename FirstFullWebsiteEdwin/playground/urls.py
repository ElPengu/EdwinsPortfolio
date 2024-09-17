from django.urls import path

from . import views
#We can reference view function

#Spell properly
urlpatterns = [
    path('hello/', views.say_hello),
    path('cssPlayground', views.cssPlayground),
]
