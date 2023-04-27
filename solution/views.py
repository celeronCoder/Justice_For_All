from django.shortcuts import render

# Create your views here.
def solution(request):
    return render(request, 'solution.html')