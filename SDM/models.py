from django.db import models

# Create your models here.
# Students Model
class Student(models.Model):
    PEN = models.BigIntegerField()
    Name = models.CharField(max_length = 30)
    Gender = models.CharField(max_length = 6)
    Email = models.CharField(max_length = 30, primary_key = True)
    Mobile = models.BigIntegerField()
    Department = models.CharField(max_length = 30)
    Semester = models.IntegerField()
    RegisterTime = models.DateTimeField(auto_now = True)

# Faculties Model
class Faculty(models.Model):
    Name = models.CharField(max_length = 30)
    Gender = models.CharField(max_length = 6)
    Email = models.CharField(max_length = 30, primary_key = True)
    Mobile = models.BigIntegerField()
    Department = models.CharField(max_length = 30)
    Password = models.CharField(max_length = 30)
    RegisterTime = models.DateTimeField(auto_now = True)
