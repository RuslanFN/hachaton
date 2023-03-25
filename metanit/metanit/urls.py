"""metanit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hello import views

import hello.viewsBD.classesviews as classes
import hello.viewsBD.classroomsviews as classrooms
import hello.viewsBD.coursesviews as courses
import hello.viewsBD.groupviews as groups
import hello.viewsBD.teachersviws as teachers


classes_patterns = [
    path('delete', classes.delete),
    path('create', classes.create)
]

classrooms_patterns = [
    path('delete', classrooms.delete),
    path('create', classrooms.create)
]

courses_patterns = [
    path('delete', courses.delete),
    path('create', courses.create)
]

groups_patterns = [
    path('delete', groups.delete),
    path('create', groups.create)
]

teachers_patterns = [
    path('delete', teachers.delete),
    path('create', teachers.create)
]

urlpatterns = [
    path('', views.list_groups, name='Home'),
    path('timetable/<int:id>', views.timetable),
    path('admin/', admin.site.urls),
    path('class/', include(classes_patterns)),
    path('classroom/', include(classrooms_patterns)),
    path('cours/', include(courses_patterns)),
    path('groups/', include(groups_patterns)),
    path('teacher/', include(teachers_patterns))
]
