from django.contrib import admin
from newapp.models import Employee,Workhour,Salary,Signup
# Register your models here.

admin.site.register(Employee)
admin.site.register(Workhour)
admin.site.register(Salary)
admin.site.register(Signup)