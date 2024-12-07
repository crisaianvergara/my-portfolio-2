from django.db import models


class Resume(models.Model):
    upload_date = models.DateTimeField(auto_now=True)
    resume_file = models.FileField(upload_to="resumes/", null=True, blank=True)