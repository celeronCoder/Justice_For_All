from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, "index.html" )

def signup(request):
    return render(request,"signup_page.html")

def signin(request):
    return render(request,"login.html")

def logout(request):
    return render(request, "index.html")

def home_page(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def gallery(request):
    return render(request, "gallery.html")
