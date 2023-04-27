from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
# Create your views here.
def contact(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.phone=phone
        contact.save()
        return HttpResponse("<h1> Thanks for contacting us </h1>")
    return render(request, 'index.html') 
    