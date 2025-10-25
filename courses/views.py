from django.shortcuts import render
from django.views.generic import ListView
from .models import Course
from tutors.models import Tutor
from schools.models import School
from .choices import district_choices, subject_choices


def courses(request):
    courses = Course.objects.all()
    mvp_tutors = Tutor.objects.all().filter(is_mvp=True)

    context = {
        'courses': courses,
        'mvp_tutors': mvp_tutors,
    }
    return render(request, 'courses/courses.html', context)


def course(request, course_id):
    course = Course.objects.get(id=course_id)
    mvp_tutors = Tutor.objects.all().filter(is_mvp=True)
    context = {
        'course': course,
        'mvp_tutors': mvp_tutors,
    }
    return render(request, 'courses/course.html', context)
