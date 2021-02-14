from django.shortcuts import render
from django.http import HttpResponse, request
from .models import subjects_list
from .models import marks

# Create your views here.
def home(request):
    return render(request, 'home.html')

def years_list_view(request):
    return render(request, 'years_list.html')

def sub_list_view(request): 
    data = subjects_list.objects.all()
    stu = {
        "student_name":data
    }
    return render(request, 'sub_list.html', stu)

def view_student(request):
    data = marks.objects.all()
    stu = {
        "student":data
    }
    return render(request, 'view_student.html', stu)

def sem_marks_view(request):
    return render(request,'sem_marks.html')

def marks_edit_view(request):
    return render(request, 'marks_edit.html')
