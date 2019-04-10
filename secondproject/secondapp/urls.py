from django.urls import path
from secondapp import views


urlpatterns=[
    path('', views.template, name="index"),
    path('Firstapp', views.index1, name="index1"),
    path('Secondapp', views.index2, name="index2"),
    path('Thirdapp', views.index3, name="index3"),

]