from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('home',views.home, name='home'),
    path('student_detail',views.student_detail,name='student_detail'),
    path('marks_detail',views.marks_detail,name='marks_detail'),
    path('time_table',views.time_table,name='time_table'),
    path('add_student_detail',views.add_student_detail,name='add_student_detail'),
    path('add_marks',views.add_marks,name='add_marks'),
    path('view_students',views.view_students,name='view_students'),
    path('view_marks',views.view_marks,name='view_marks'),
    path('delete_student',views.delete_student,name='delete_student'),
    path('delete_marks',views.delete_marks,name='detele_marks'),
    path('update_marks',views.update_marks,name='update_marks'),
    path('update_student',views.update_student,name='update_student'),
    path('attendance',views.attendance,name='attendance'),
    
]


