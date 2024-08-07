# Generated by Django 5.0.2 on 2024-07-24 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_remove_tag_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='project_images'),
        ),
        migrations.AlterField(
            model_name='project',
            name='repo',
            field=models.URLField(blank=True, max_length=255),
        ),
    ]
