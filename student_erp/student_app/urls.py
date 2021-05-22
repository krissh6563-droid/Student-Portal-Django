from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('student_detail',views.student_detail,name='student_detail'),
    path('marks_detail',views.marks_detail,name='marks_detail'),
    path('time_table',views.time_table,name='time_table')
    
]