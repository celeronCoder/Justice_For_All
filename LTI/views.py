from django.shortcuts import render

# Create your views here.
def LTI(request):
    return render(request, 'LTI.html')  