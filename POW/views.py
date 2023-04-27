from django.shortcuts import render

# Create your views here.
def POW(request):
    return render(request, 'POW.html')  