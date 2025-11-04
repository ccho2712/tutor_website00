from django.shortcuts import render
from tutors.models import Tutor
from courses.models import Course
from courses.choices import district_choices, subject_choices

# Create your views here.


def index(request):
    courses = Course.objects.all()[:4]
    tutors = Tutor.objects.all()[:4]
    context = {
        'courses': courses,
        'tutors': tutors,
        'district_choices': district_choices,
        'subject_choices': subject_choices,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    tutors = Tutor.objects.all()[:4]

    context = {
        'tutors': tutors,
    }
    return render(request, 'pages/about.html', context)


def contact(request):
    return render(request, 'pages/contact-us.html')


def copyright(request):
    return render(request, 'pages/copyright.html')


def terms_of_use(request):
    return render(request, 'pages/terms_of_use.html')


def privacy(request):
    return render(request, 'pages/privacy.html')
