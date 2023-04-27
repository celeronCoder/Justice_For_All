from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('sup', views.sup, name = "Sign Up" ) ,
    path('sin', views.sin, name = "Sign In" ) ,
    path('sout', views.sout, name = "Log Out"),
]
