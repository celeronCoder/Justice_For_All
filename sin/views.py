from django.shortcuts import render

# Create your views here.
def sin(request):
    return render(request, 'sin.html') 