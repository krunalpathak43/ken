from django.urls import path
from newapp import views

urlpatterns = [
    path('/arpit',views.index, name="index"),
    path('Firstapp', views.index1, name="index1"),
    path('Secondapp', views.index2, name="index2"),
    path('',views.template_demo, name="index"),

]