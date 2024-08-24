from django.contrib import admin

from .models import Project, Tag


@admin.register(Tag)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "create_uid")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "display_project", "create_date", "create_uid")