from django.shortcuts import render
from django.views.generic import ListView
from .models import Course
from tutors.models import Tutor
from schools.models import School
from .choices import district_choices, subject_choices
from django.db.models import Q
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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


def search(request):
    queryset_list = Course.objects.order_by('-created_at')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(Q(school__title__icontains=keywords) | Q(
                title__icontains=keywords) | Q(tutor__name__icontains=keywords))
    if 'district' in request.GET:
        district = request.GET['district']
        if district:
            queryset_list = queryset_list.filter(district__iexact=district)
    if 'subject' in request.GET:
        subject = request.GET['subject']
        if subject:
            queryset_list = queryset_list.filter(subject__iexact=subject)

    # paginator = Paginator(queryset_list, 3)
    # page = request.GET.get('page')
    # paged_courses = paginator.get_page(page)
    context = {
        # 'courses': paged_courses,
        'courses': queryset_list,
        'district_choices': district_choices,
        "subject_choices": subject_choices,
        "values": request.GET,
    }
    return render(request, 'courses/search.html', context)
