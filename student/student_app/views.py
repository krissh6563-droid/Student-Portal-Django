from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from .models import Students_detail, Time_table
from .models import Marks_detail
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.

def home(request):
    return render(request,'home.html')

def student_detail(request):
    return render(request,'student_detail.html')

def marks_detail(request):
    return render(request,'marks.html')

def time_table(request):
    row = Time_table.objects.all()
   
    return render(request,'time_table.html',{'data':row})

def login(request):
    if request.method=='POST':
        user = request.POST['username']
        pass_1 = request.POST['password']
        user = auth.authenticate(username = user,password=pass_1)
        if user is not None:
            auth.login(request,user)
            return render(request,'home.html')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def view_students(request):
    if request.method=='POST':
        study_year = request.POST['year']
        roll_no = request.POST['roll_number']
        row = Students_detail.objects.filter(roll_number = roll_no)
        return render(request, 'student_detail.html',{'data':row})

def add_student_detail(request):
    if request.method=='POST':
        s_roll = request.POST['roll_number']
        s_name = request.POST['student_name']
        s_father_name = request.POST['father_name']
        s_study_year = request.POST['year']
        s_mobile = request.POST['mobile_number']
        s_gmail = request.POST['email']
        s_add = request.POST['address']
        student_info = Students_detail(roll_number=s_roll,student_name = s_name, year = s_study_year,father_name = s_father_name,mobile_number = s_mobile,mail=s_gmail,address=s_add)
        student_info.save()
        messages.success(request, "Record added Successfully")
        return render(request,'student_detail.html')

def update_student(request):
    pass


def delete_student(request):
    if request.method=='POST':
        roll_no = request.POST['roll_number']
        temp = Students_detail.objects.get(roll_number=roll_no)
        temp.delete()
        messages.success(request, "Record deleted Successfully")
        return render(request,'student_detail.html')
    
def view_marks(request):
    if request.method=='POST':
        study_year = request.POST['year']
        subject = request.POST['subject']
        exam = request.POST['exam_type']
        row = Marks_detail.objects.filter(year=study_year,subject_name=subject,exam_type=exam)
        return render(request,'marks.html',{'data':row})

def add_marks(request):
    if request.method=='POST':
        m_roll = request.POST['roll_number']
        m_name = request.POST['student_name']
        m_year  = request.POST['year']
        m_sub = request.POST['subject']
        m_exam_type = request.POST['exam_type']
        m_obt_marks = request.POST['obtained_marks']
        m_total_marks = request.POST['total_marks']
        marks_info = Marks_detail(roll_number = m_roll, student_name = m_name, year = m_year,subject_name = m_sub, exam_type = m_exam_type,total_marks= m_total_marks,obtained_marks = m_obt_marks)
        marks_info.save()
        messages.success(request, "Record added Successfully")
        return render(request,'marks.html')

def update_marks(request):
    if request.method=='POST':
        roll_no = request.POST['roll_number']
        sub_name = request.POST['subject_name']
        ex_type = request.POST['exam_type']
        obt_marks = request.POST['obtained_marks']
        temp = Marks_detail.objects.get(roll_number = roll_no,subject_name=sub_name,exam_type=ex_type)
        temp.obtained_marks = obt_marks
        temp.save()
        messages.success(request, "Record updated Successfully")
        return render(request,'marks.html')
        

def delete_marks(request):
    if request.method=='POST':
        roll_no = request.POST['roll_number']
        sub_name = request.POST['subject_name']
        ex_type = request.POST['exam_type']
        temp = Marks_detail.objects.filter(roll_number = roll_no,subject_name=sub_name,exam_type=ex_type)
        temp.delete()
        messages.success(request, "Record deleted Successfully")
        return render(request,'marks.html')








    


