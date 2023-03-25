from typing import Any
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=50)
class Classroom(models.Model):
    name = models.CharField(max_length=10)

class Group(models.Model):
    name = models.CharField(max_length=20)
    courses = models.ManyToManyField(Course)

class Teacher(models.Model):
    name = models.CharField(max_length=40)
    course = models.ManyToManyField(Course)

class Class(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    time = models.TimeField()

# Create your models here.
