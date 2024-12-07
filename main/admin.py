from django.contrib import admin

from .models import Resume


@admin.register(Resume)
class MainAdmin(admin.ModelAdmin):
    list_display = ("upload_date", "resume_file")
