from django.shortcuts import render
from django.http import FileResponse, Http404 

from .models import Resume


def index(request):
    context = {"title": "Home"}
    return render(request, "main/index.html", context)


def resume(request):
    resume = Resume.objects.last()
    if resume and resume.resume_file:
        try:
            response = FileResponse(resume.resume_file, content_type='application/pdf', as_attachment=False)
            return response
        except Exception:
            raise Http404("Resume file not found.")
    raise Http404("No resume available.")