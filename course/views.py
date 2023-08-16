from django.shortcuts import render
from .models import Course
from .forms import CourseForm
from .import views
from django.shortcuts import HttpResponse, render, redirect
# Create your views here.


def index(request):
    if request.method =='POST':
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            course_model = course_form.save(commit = False)
            course_model.save()
            return HttpResponse("data submitted successfully")
        else:
            return render(request, "course/index.html", {'form':course_form})
    else:
        course_form = CourseForm(None)
        return render(request, 'course/index.html', {'form':course_form})