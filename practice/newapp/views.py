from django.shortcuts import render
from django.http import HttpResponse
from .models import  Signup
from . import forms
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


def form_view(request):
    form = forms.FormName()
    if request.method == "POST":
        form = forms.FormName(request.POST)
        if form.is_valid():

            print("Name= "+form.cleaned_data["name"])
            print(request.POST.get("name"))
            form.save()
            return HttpResponse("Your values are save")
        else:
            print(form.errors)
            return render(request,'basic_form.html',{'form1':form})
    return render(request,'basic_form.html',{'form1':form})



    return render(request,'basic_form.html',{'form1':form})