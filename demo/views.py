from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world")


def homepage(request):
    return render(request,'home.html',{"name": "oba"})