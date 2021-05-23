from django.db import models

class Students_detail(models.Model):
    roll_number = models.IntegerField()
    student_name = models.CharField(max_length=50)
    year = models.CharField(max_length=10)
    father_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

class Marks_detail(models.Model):
    roll_number = models.IntegerField()
    student_name = models.CharField(max_length=50)
    year =  models.CharField(max_length=10)
    subject_name = models.CharField(max_length=30)
    exam_type = models.CharField(max_length=30)
    total_marks = models.IntegerField()
    obtained_marks = models.IntegerField()
       
class Time_table(models.Model):
    year = models.IntegerField()
    time_table_img = models.ImageField()

    
