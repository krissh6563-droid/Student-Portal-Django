# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Students_detail
from .models import Marks_detail

# Create your views here.

def home(request):
    return render(request,'home.html')

def student_detail(request):
    return render(request,'student_detail.html')

def marks_detail(request):
    return render(request,'marks.html')

def time_table(request):
    return render(request,'time_table.html')

def add_student_detail(request):
    s_roll = request.POST['roll_number']
    s_name = request.POST['student_name']
    s_father_name = request.POST['father_name']
    s_study_year = request.POST['year']
    s_mobile = request.POST['mobile_number']
    s_gmail = request.POST['email']
    s_add = request.POST['address']
    student_info = Students_detail(roll_number=s_roll,student_name = s_name, year = s_study_year,father_name = s_father_name,mobile_number = s_mobile,mail=s_gmail,address=s_add)
    student_info.save()
    return render(request,'student_detail.html')

def add_marks(request):
    m_roll = request.POST['roll_number']
    m_name = request.POST['student_name']
    m_year  = request.POST['year']
    m_sub = request.POST['subject']
    m_exam_type = request.POST['exam_type']
    m_obt_marks = request.POST['obtained_marks']
    m_total_marks = request.POST['total_marks']
    marks_info = Marks_detail(roll_number = m_roll, student_name = m_name, year = m_year,subject_name = m_sub, exam_type = m_exam_type,total_marks= m_total_marks,obtained_marks = m_obt_marks)
    marks_info.save()
    return render(request,'marks.html')

    


