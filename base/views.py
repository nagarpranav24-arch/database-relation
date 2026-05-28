from django.shortcuts import render
from courses.models import Course
from students.models import Student

# Create your views here.

def index(request):
    courses = Course.objects.all() # this is coming from the models of course
    context = {"courses": courses} #this is the third parameter for render as a context and this context you  will reflect it in html
    print(courses)
    return render(request, "index.html", context=context)



def course_student(request, course_id):
    course = Course.objects.get(id=course_id)
    student = Student.objects.filter(courses= course)
    
    
    return render(request, "details.html", {"students":student, "course":course})


def pass_data(request, data):
    print(data)
    return render(request, "data.html", {"data": data})



