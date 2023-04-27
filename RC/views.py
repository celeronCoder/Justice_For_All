from django.shortcuts import render

# Create your views here.
def RC(request):
    return render(request, 'RC.html')  