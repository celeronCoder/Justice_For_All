from django.shortcuts import render

# Create your views here.
def sup(request):
    return render(request, 'sup.html')  