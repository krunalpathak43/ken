
from django.shortcuts import render, redirect
from mainapp.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . import views
from . import forms


# Create your views here.
def index(request):
    return HttpResponse("This is from index page")

def template(request):
    dist_var={'any_key':"Hello World!"}
    return render(request,'mainapp/index.html', context=dist_var)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'mainapp/login.html', {'any_form_key':form})




def form_view(request):
    form = forms.FormName()
    if request.method == "POST":
        form = forms.FormName(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
        return redirect ('/index',pk=post.pk)

    return render(request,'mainapp/signup.html',{'any_form_key':form})
