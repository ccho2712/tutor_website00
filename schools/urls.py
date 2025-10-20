from django.urls import path
from . import views

app_name = 'schools'

urlpatterns = [
    path('', views.schools, name='schools'),
    path('<int:school_id>/', views.school, name='school'),
]