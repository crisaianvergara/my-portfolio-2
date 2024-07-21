from django.shortcuts import render
from .utils import projects


def index(request):
    context = {"projects": projects,"title": "Projects"}
    return render(request, "projects/index.html", context)
