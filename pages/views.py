from django.shortcuts import render
from tutors.models import Tutor
from courses.models import Course

# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    mvp_tutors = Tutor.objects.all().filter(is_mvp=True)
    context = {
        'mvp_tutors': mvp_tutors,
    }
    return render(request, 'pages/about.html', context)


def contact(request):
    return render(request, 'pages/contact-us.html')
