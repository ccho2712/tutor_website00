from django.shortcuts import render, get_object_or_404
from .models import School
from tutors.models import Tutor
from courses.models import Course
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
# Create your views here.


def schools(request):
    # schools = School.objects.all()
    schools = School.objects.order_by('title').filter(is_published=True)
    paginator = Paginator(schools, 3)
    page = request.GET.get('page')
    paged_schools = paginator.get_page(page)
    context = {"schools": paged_schools}
    return render(request, 'schools/schools.html', context)


def school(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    courses = Course.objects.filter(school=school)[:3]
    context = {"school": school, "courses": courses}
    return render(request, 'schools/school.html', context)
