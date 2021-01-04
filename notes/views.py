from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('123')

def page(request):
    return render(request,'notes/default.html')
