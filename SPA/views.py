from django.shortcuts import render

# Create your views here.
def SPA(request):
    return render(request, 'SPA.html')  