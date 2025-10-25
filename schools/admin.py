from django.contrib import admin

# Register your models here.
from .models import School
from django.forms import NumberInput
from django.db import models


class SchoolAdmin(admin.ModelAdmin):
    # form = SchoolAdminForm
    list_display = ('id', 'title', 'district', 'is_published')
    list_display_links = ('id', 'title')
    # list_filter = ("tutor",'services')
    list_editable = ("is_published",)
    search_fields = ('title', 'district', 'tutor__name',
                     'services__name', 'professionals__name')
    list_per_page = 25
    ordering = ['-id']
    # prepopulated_fields = {'title': ('title',)}
    formfield_overrides = {
        models.IntegerField: {
            'widget': NumberInput(attrs={'size': '10'})
        },
    }
    show_facets = admin.ShowFacets.ALWAYS


admin.site.register(School, SchoolAdmin)
