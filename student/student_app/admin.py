from django.contrib import admin
from .models import Students_detail
from .models import Marks_detail
from .models import Time_table
from .models import Subject_list
# Register your models here.

admin.site.register(Students_detail)
admin.site.register(Marks_detail)
admin.site.register(Time_table)
admin.site.register(Subject_list)

