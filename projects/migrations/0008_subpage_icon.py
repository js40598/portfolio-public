# Generated by Django 3.0.3 on 2020-08-21 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_remove_project_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='subpage',
            name='icon',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
