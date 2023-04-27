from django.shortcuts import render

# Create your views here.
def advocate(request):
    return render(request, 'advocate.html')