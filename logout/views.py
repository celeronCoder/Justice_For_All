from django.shortcuts import render

# Create your views here.
def logoutaction(request):
    return render(request,'index_page.html') 