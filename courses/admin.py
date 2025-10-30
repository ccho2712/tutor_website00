from django.contrib import admin
from .models import Course, Curriculum
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'tutor', 'students_enrolled',
                    'max_students', 'rating', 'price', 'duration', 'class_type', 'subject', 'district', 'school')
    list_display_links = ('title', )
    list_editable = ('tutor', 'price', 'duration', 'subject', 'district', 'school',
                     'class_type', 'students_enrolled')


class CurriculumAdmin(admin.ModelAdmin):
    list_display = ('name', 'text')
    list_display_links = ('name', )
    list_editable = ('name',)


admin.site.register(Course, CourseAdmin)
admin.site.register(Curriculum, CurriculumAdmin)
