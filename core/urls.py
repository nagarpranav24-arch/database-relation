
from django.contrib import admin
from django.urls import path
from base.views import *
from teachers.views import *
from students.views import *
from courses.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="homepage"),
    path('teacher/', teacher, name="teacher"),
    path('student/', student, name="student"),
    path('course/', course, name="course"),
]
