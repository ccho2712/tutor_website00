from django.shortcuts import render


def schools(request):
    return render(request, 'schools/schools.html')

def school(request):
    return render(request, 'schools/school.html')

# Create your views here.
