from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name = 'home'),
    path('years_list', views.years_list_view, name = 'years_list'),
    path('sub_list',views.sub_list_view, name = 'sub_list'),
    path('view_student',views.view_student, name = 'view_student'),
    path('sem_marks',views.sem_marks_view,name = 'sem_marks'),
    path('marks_edit',views.marks_edit_view , name = 'marks_edit'),
    
]