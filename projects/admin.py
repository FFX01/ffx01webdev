from django.contrib import admin
from .models import Project, ProjectComments

class ProjectAdmin(admin.ModelAdmin):
    exclude = [
        'slug'
    ]

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectComments)
