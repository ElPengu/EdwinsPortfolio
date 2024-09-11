from django.urls import path

from . import views
#We can reference view function

#Spell properly
urlpatterns = [
    path('', views.mainPageView, name='mainPage'),
    path('register/', views.registerPageView, name='registerPage'),
    path('success/', views.successPageView, name='successPage')
]
