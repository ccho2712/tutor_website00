from django.shortcuts import render
from django.views.generic import ListView
from .models import Tutor
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def tutors(request):
    tutors = Tutor.objects.all()
    items_per_page = int(request.GET.get('items_per_page', 4))
    paginator = Paginator(tutors, items_per_page)
    page = request.GET.get('page', 1)
    paged_tutors = paginator.get_page(page)
    context = {
        'tutors': paged_tutors,

    }
    return render(request, 'tutors/tutors.html', context)


def tutor(request, tutor_id):
    tutor = Tutor.objects.get(id=tutor_id)
    return render(request, 'tutors/tutor.html', {'tutor': tutor})
