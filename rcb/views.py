from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def virat(request):
    return HttpResponse('<h1>virat is king in cricket<h1>')
def surya(request):
    return render (request,'surya.html')