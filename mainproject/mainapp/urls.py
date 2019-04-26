from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'mainapp'

urlpatterns=[
    path('index',views.index, name='index'),
    path('',views.template, name='index1'),
    path('signup/', views.form_view, name='signup'),
    path('about/', TemplateView.as_view(template_name='mainapp/about.html')),
    path('gallery/', TemplateView.as_view(template_name='mainapp/gallerynew.html')),
    path('login/',TemplateView.as_view(template_name='mainapp/login.html')),
    url(r'^user_login/$', views.user_login, name='user_login'),

]