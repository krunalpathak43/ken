from django.contrib import admin
from secondapp.models import Employee,Workhour,Salary
# Register your models here.
admin.site.register(Employee)
admin.site.register(Workhour)
admin.site.register(Salary)