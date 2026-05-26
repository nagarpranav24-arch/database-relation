from django.shortcuts import render, redirect
from teachers.models import Teacher
from courses.models import Course
from .models import Student

# Create your views here.

def student(request):
    teachers = Teacher.objects.all()
    courses = Course.objects.all()
    if request.method == "POST":
        student_name = request.POST.get("student_name")
        get_teacher = request.POST.get("teacher")
        selected_teacher = Teacher.objects.get(id=get_teacher)
        course = request.POST.get("course")
        students =Student.objects.create(name=student_name, teacher=selected_teacher)
        students.courses.set(course)
        students.save()
        return redirect("homepage")
    return render(request, "student.html", {"teachers":teachers, "courses": courses})