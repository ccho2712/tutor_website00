from django.contrib import admin
from .models import Tutor
# Register your models here.


class TutorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_mvp', 'phone', 'course_subject',
                    'rating', 'experience', 'taught_students')
    list_display_links = ('name',)
    list_editable = ('is_mvp', 'course_subject', 'rating',
                     'experience', 'taught_students')


admin.site.register(Tutor, TutorAdmin)
