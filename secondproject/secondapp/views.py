from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello Guys.")
def index1(request):
    return HttpResponse("Hello Guys!This is my first application.")
def index2(request):
    return HttpResponse("Hello Guys!This is my second application.")
def index3(request):
    return HttpResponse("Hello Guys!This is my third application.")

def template(request):
    dict_var={'random_var':" I am written in views.py"}
    return render(request,'tempapp/index.html', context=dict_var)