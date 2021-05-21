from django.contrib import admin
from .models import  Students_detail, marks_detail,time_table
# Register your models here.

admin.site.register(Students_detail)
admin.site.register(marks_detail)
admin.site.register(time_table)

