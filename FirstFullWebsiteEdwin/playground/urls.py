from django.urls import path

from . import views

#Import decorators from decoractors.py
from .decorators import superuser_only

#We can reference view function

#We want to lock non-superusers from this app
def dec_patterns(patterns):
    decorated_patterns = []
    for pattern in patterns:
        callback = pattern.callback
        pattern.callback = superuser_only(callback)
        pattern._callback = superuser_only(callback)
        decorated_patterns.append(pattern)
    return decorated_patterns


#Spell properly
urlpatterns = [
    path('hello/', views.say_hello),
    path('cssPlayground', views.cssPlayground),
]
urlpatterns = dec_patterns(urlpatterns)