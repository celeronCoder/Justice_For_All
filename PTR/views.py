from django.shortcuts import render

# Create your views here.
def PTR(request):
    return render(request, 'PTR.html')  