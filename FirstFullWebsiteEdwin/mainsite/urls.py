from django.urls import path, include

from . import views
#We can reference view function

#Spell properly
urlpatterns = [
    path('', views.mainPageView, name='mainPage'),
    path('register/', views.registerPageView, name='registerPage'),
    path('login/', views.loginPageView, name='loginPage'),
    path('logout/', views.logoutPageView, name='logoutPage'),
    path('success/', views.successPageView, name='successPage'),
    path('dashboard/', views.dashboardPageView, name='dashboardPage'),
    #For to-do list stuff
    path('todolist', include('todolistsite.urls')),
    
]
