from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('home',views.home, name='home'),
    path('student_detail',views.student_detail,name='student_detail'),
    path('marks_detail',views.marks_detail,name='marks_detail'),
    path('time_table',views.time_table,name='time_table'),
    path('add_student_detail',views.add_student_detail,name='add_student_detail'),
    path('add_marks',views.add_marks,name='add_marks'),
    path('view_students',views.view_students,name='view_students'),
    path('view_marks',views.view_marks,name='view_marks'),

    
]
