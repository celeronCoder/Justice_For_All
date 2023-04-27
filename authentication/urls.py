from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name = "Sign Up" ) ,
    path('signin', views.signin, name = "Sign In" ) ,
    path('logout', views.logout, name = "Log Out"),
    path('home_page', views.home_page, name="Home Page"),
    path('contact', views.contact, name="contact"),
    path('gallery', views.gallery, name = "gallery"),
]

