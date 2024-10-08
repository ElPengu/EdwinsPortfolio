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
    path('todolist/', include('todolistsite.urls')),
    #If a user tries to do superuser stuff
    path('nonsuperuser/', views.nonsuperuserPageView, name='nonsuperuserPage'),
    path('contactus/', views.contactusPageView, name='contactusPage'),
    
    #For personal details stuff
    path('personaldetails/', include('personaldetailssite.urls'))
]
