from django.db import models
from django.db.models.signals import pre_save

from projects.models import Project

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    in_html = models.CharField(max_length=150, blank=True)
    priority = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    IS_DONE_CHOICES = [('DONE', 'Done'), ('ONGOING', 'Ongoing'), ('FUTURE', 'Future')]
    is_done = models.CharField(max_length=10, choices=IS_DONE_CHOICES, default='FUTURE')


def in_html_generator(sender, instance, *args, **kwargs):
    instance.in_html = '<li>'+instance.title+'</li>'


pre_save.connect(in_html_generator, sender=Task)
