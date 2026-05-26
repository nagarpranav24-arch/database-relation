from django.shortcuts import render, redirect
from .models import Teacher

# Create your views here.

def teacher(request):
    if request.method == "POST":
        teacher_name = request.POST.get("teacher_name")
        teachers = Teacher.objects.create(name=teacher_name)
        teachers.save()
        return redirect("homepage")
    return render(request, "teacher.html")