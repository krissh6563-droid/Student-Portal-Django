from django.db import models

# Create your models here.

class subjects_list(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class marks(models.Model):
    roll_number  = models.IntegerField(max_length=200,primary_key=True)
    student_name = models.CharField(max_length=200,)
    test_1 = models.IntegerField(max_length=100)
    test_2 = models.IntegerField(max_length=100)
    pre_exam_1 = models.IntegerField(max_length=100)
    test_3 = models.IntegerField(max_length=100)
    test_4 = models.IntegerField(max_length=100)
    pre_exam_2 = models.IntegerField(max_length=100)

    def __str__(self):
        return self.student_name
