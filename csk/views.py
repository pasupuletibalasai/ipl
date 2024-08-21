from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dhoni(request):
    return HtttpResponse('<h1>dhoni is good wicket keeper</h>')
def raina(request):
    return render(request,'raina.html')    