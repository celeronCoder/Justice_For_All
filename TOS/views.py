from django.shortcuts import render

# Create your views here.
def TOS(request):
    return render(request, 'TOS.html')  