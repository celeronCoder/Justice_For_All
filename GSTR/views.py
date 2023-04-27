from django.shortcuts import render

# Create your views here.
def GSTR(request):
    return render(request, 'GSTR.html')  