from django.shortcuts import render

from .models import Project


def index(request):
    projects = Project.objects.order_by("name").all()
    context = {"projects": projects, "title": "Projects"}
    return render(request, "projects/index.html", context)