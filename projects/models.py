from django.db import models
from datetime import datetime
from django.db.models.signals import pre_save
from portfolio.utils import unique_slug_generator, unique_url_generator, non_unique_slug_generator

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True, default=None)
    icon = models.CharField(max_length=50, blank=True)
    github_url = models.CharField(max_length=250, blank=True)
    init_date = models.DateField(default=datetime.now, blank=True)
    planned_finish_date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title


class Subpage(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True, default=None)
    url = models.CharField(max_length=100, null=True, blank=True, default=None)
    icon = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)


def slug_generator(sender, instance, *args, **kwargs):
    if sender == Subpage:
        unique = False
    else:
        unique = True

    if unique == True:
        if not instance.slug:
            instance.slug = unique_slug_generator(instance)
    else:
        if not instance.slug:
            instance.slug = non_unique_slug_generator(instance)


def url_generator(sender, instance, *args, **kwargs):
    if not instance.url:
        instance.url = unique_url_generator(instance)


pre_save.connect(slug_generator, sender=Project)
pre_save.connect(slug_generator, sender=Subpage)
pre_save.connect(url_generator, sender=Subpage)
