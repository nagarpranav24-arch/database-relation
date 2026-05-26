from django.shortcuts import render, redirect
from .models import Course

# Create your views here.


def course(request):
    if request.method == "POST":
        course_name = request.POST.get("course_name")
        courses = Course.objects.create(name=course_name)
        courses.save()
        return redirect("homepage")
    return render(request, "course.html")