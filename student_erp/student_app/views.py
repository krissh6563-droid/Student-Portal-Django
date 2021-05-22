from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.

def home(request):
    return render(request,'home.html')

def student_detail(request):
    return render(request,'student_detail.html')

def marks_detail(request):
    return render(request,'marks.html')

def time_table(request):
    return render(request,'time_table.html')

