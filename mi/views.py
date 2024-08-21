from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rohit(request):
    return HttpResponse('<h1>rohit is hitman</h1>')
def harthik(request):
    return render(request,'harthik.html')    