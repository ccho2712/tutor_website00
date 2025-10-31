from django.db import models
from datetime import datetime
from courses.choices import subject_choices
# Create your models here.


class Tutor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20, default='00000000')
    email = models.EmailField(max_length=50, unique=False, blank=True)
    is_mvp = models.BooleanField(default=True)
    hire_date = models.DateTimeField(auto_now_add=True)
    course_subject = models.CharField(max_length=50,
                                      choices=subject_choices,
                                      default='Chinese',
                                      help_text='Subject taught by the tutor'
                                      )
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=0.0,
        help_text='Average rating from 0.0 to 5.0'
    )
    experience = models.CharField(
        max_length=20,
        default=1,
        help_text='Years of experience'
    )
    taught_students = models.PositiveIntegerField(
        default=100,
        help_text='Number of students taught'
    )

    def __str__(self):
        return self.name
