from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
    return render(request, 'post/hello.html')

def golden(request):
    return render(request, 'post/golden.html')

def greet(request):
    return HttpResponse("Welcome to django class")

def love(request):
    return HttpResponse("I'm in love with a church girl")
