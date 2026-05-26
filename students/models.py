from django.db import models
from teachers.models import Teacher
from courses.models import Course

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name