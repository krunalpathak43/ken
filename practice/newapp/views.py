from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse(" Hello there! Just Practice")
def index1(request):
    return HttpResponse(" Hello Guys! This is my first practice app")
def index2(request):
    return HttpResponse(" Hello Guys! This is my second practice app")

def template_demo(request):
    dict_var = {'random_var':" I am written in views!"}
    return render(request,'index1.html', context=dict_var)