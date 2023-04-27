from django.shortcuts import render

# Create your views here.
def IP(request):
    return render(request, 'IP.html')  