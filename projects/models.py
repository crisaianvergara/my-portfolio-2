from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    create_uid = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="created_tags")
    write_date = models.DateTimeField(auto_now=True)
    write_uid = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="written_tags")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('tag-detail', args=[str(self.id)])
    
    class Meta:
        constraints = [
            UniqueConstraint(
                Lower("name"),
                name = "tag_name_case_insensitive_unique",
                violation_error_message = "Tag already exists (case insensitive match)."
            )
        ]


class Project(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="project_images")
    description = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)
    site = models.URLField(max_length=255)
    repo = models.URLField(max_length=255, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    create_uid = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="created_projects")
    write_date = models.DateTimeField(auto_now=True)
    write_uid = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="written_projects")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('project-detail', args=[str(self.id)])
    
    def display_project(self):
        return ", ".join(tag.name for tag in self.tags.all())
    
    display_project.short_description = "Tags"

