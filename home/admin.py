from django.contrib import admin
from home.models import students
# Register your models here.
@admin.register(students)
class studentsAdmin(admin.ModelAdmin):
    list_display=("id","name","email","phone","country","department")