from django.contrib import admin
from newapp.models import Employee,Workhour,Salary
# Register your models here.

admin.site.register(Employee)
admin.site.register(Workhour)
admin.site.register(Salary)