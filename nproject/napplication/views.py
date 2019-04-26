from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("I am from Index")

def temp_demo(request):
    dict_var={'any_key':"I am a value from view.py"}
    return render(request,'napplication/base.html', context=dict_var)
