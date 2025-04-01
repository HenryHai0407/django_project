from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def calculate():
    x = 100
    y = 200
    return x


def say_hello(request):
    a = calculate()
    return render(request,'hello.html',{'name':'Harry Potter'})