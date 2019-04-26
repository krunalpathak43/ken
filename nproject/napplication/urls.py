from django.urls import path
from napplication import views


urlpatterns=[

    path('admin/',views.index, name='index'),
    path('',views.temp_demo, name='index')

]
