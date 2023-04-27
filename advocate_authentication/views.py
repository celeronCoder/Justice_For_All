from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.
def home(request):
    return render(request,"index.html")

def sin(request):

    if request.method == "POST":
        bar = request.POST['bar']
        psw = request.POST['psw']

        user = authenticate(bar=bar, psw=psw)

        if user is not None:
            login(request, user)
            name =  user.name 
            return render(request,"index.html", {'name':name})

        else:
            messages.error(request, "Bad Credentials")
            return redirect ('home')
    return render(request,"sin.html")

def sup(request):

    if request.method == "POST":
        name =  request.POST['name']
        email =  request.POST['email']
        phone = request.POST['phone']
        court = request.POST['court']
        bar = request.POST['bar']
        image = request.POST['image'] 
        psw = request.POST['psw']
        pswr = request.POST['pswr']

        useradv = User.objects.create_user(name,email,phone,court,bar,psw)

        useradv.save()

        messages.success(request, " Your Account has been created successfully")

        return redirect('sin.html')

    return render(request,"sup.html")

def sout(request):
    pass