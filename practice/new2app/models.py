from django.db import models

# Create your models here.

class StudentName(models.Model):
    student_name=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.student_name

class ExamTime(models.Model):
    student_name=models.ForeignKey(StudentName, on_delete=models.PROTECT)
    days=models.DateTimeField('date')
    hours=models.IntegerField

    def __int__(self):
        return self.days

class Marks(models.Model):
    days=models.ForeignKey(ExamTime, on_delete=models.PROTECT)
    Getting_marks=models.IntegerField()
    result_date=models.DateField()