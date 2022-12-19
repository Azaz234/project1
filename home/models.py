from django.db import models

# Create your models here.
class students(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    country=models.CharField(max_length=100)
    department=models.CharField(max_length=100)