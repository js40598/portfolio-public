# Generated by Django 3.0.3 on 2020-08-16 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='about',
        ),
    ]
