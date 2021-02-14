from django.contrib import admin

# Register your models here.
from .models import subjects_list
from .models import marks

admin.site.register(subjects_list)
admin.site.register(marks)
