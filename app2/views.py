from django.shortcuts import render
from .models import Class
from app1.models import Student

# Create your views here.


def home(request):
    student = Student.objects.get(id=1)
    students = Student.objects.all()
    subjects = student.subject.all()
    classlevel = Class.objects.get(id=2)
    teachers = classlevel.teacher.all()
    context = {'students': students, 'classlevel': classlevel,
               'subjects': subjects, 'teachers': teachers}
    return render(request, 'index.html', context)
