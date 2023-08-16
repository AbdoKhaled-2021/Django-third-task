from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from .import views
from django.shortcuts import HttpResponse, render, redirect
# Create your views here.


def index(request):
    if request.method =='POST':
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_model = student_form.save(commit = False)
            student_model.save()
            return HttpResponse("data submitted successfully")
        else:
            return render(request, "student/index.html", {'form':student_form})
    else:
        student_form = StudentForm(None)
        return render(request, 'student/index.html', {'form':student_form})