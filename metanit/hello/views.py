from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, Group, Classroom, Class, Teacher
from datetime import datetime
import json
import logging
days = {0: 'Понедельник', 1: 'Вторник', 2: 'Среда', 3: 'Четверг', 4: 'Пятница', 5: 'Суббота', 6: 'Воскресенье'}
def index(request):
    return HttpResponse("<h2>Главная</h2>")

def list_groups(request):
    groups = Group.objects.all()
    return render(request, template_name='list_group.html', context={'groups':groups})

def timetable(request, id):
    classes = Class.objects.filter(group=id)
    weekdays = {'Понедельник': [], 'Вторник': [], 'Среда': [], 'Четверг': [], 'Пятница': [], 'Суббота': [], 'Воскресенье': []}
    for cls in classes:
        weekdays[days[datetime.weekday(cls.date)]].append(cls)
    
    for day in weekdays:
        weekdays[day].sort(key = lambda x: x.time)
    print(weekdays)
    return render(request, 'timetable.html', context={'timetable': weekdays})
        

    
 

