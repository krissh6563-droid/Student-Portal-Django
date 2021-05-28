from django.db import models
from django.db.models.base import Model

class Students_detail(models.Model):
    roll_number = models.BigIntegerField()
    student_name = models.CharField(max_length=50)
    year = models.CharField(max_length=10)
    father_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name

class Marks_detail(models.Model):
    roll_number = models.BigIntegerField()
    student_name = models.CharField(max_length=50)
    year =  models.CharField(max_length=10)
    subject_name = models.CharField(max_length=30)
    exam_type = models.CharField(max_length=30)
    total_marks = models.IntegerField()
    obtained_marks = models.IntegerField()

    def __str__(self):
        return self.student_name
       
class Time_table(models.Model):
    year = models.IntegerField()
    time_table_img = models.ImageField()

   

class Subject_list(models.Model):
    name  = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

    
