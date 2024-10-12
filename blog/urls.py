
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # path("",views.test),
    path("loginn/",views.loginn),
    path("",views.signup),
    path("home/",views.home),
    path("mypost/",views.myPost),
    path("newpost/",views.newPost),
    path("signout/",views.signOut),
]
