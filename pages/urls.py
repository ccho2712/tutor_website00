from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('copyright/', views.copyright, name='copyright'),
    path('terms_of_use/', views.terms_of_use, name='terms_of_use'),
    path('privacy/', views.privacy, name='privacy'),
]
