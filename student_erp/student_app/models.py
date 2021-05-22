from django.db.models.fields import IntegerField
#from student_erp import student_erp
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import SET_DEFAULT


# Create your models here.
class Students_detail(models.Model):
    roll_number = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=50)
    year = models.IntegerField()
    father_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name

class marks_detail(models.Model):
    roll_number = models.IntegerField()
    student_name = models.CharField(max_length=50)
    year =  models.IntegerField()
    subject_name = models.CharField(max_length=30)
    exam_type = models.CharField(max_length=30)
    total_marks = models.IntegerField()
    obtained_marks = models.IntegerField()

    def __str__(self):
        return self.student_name

class time_table(models.Model):
    year = models.IntegerField(primary_key=True)
    time_table_img = models.ImageField()

    def __str__(self):
        return self.year

    
