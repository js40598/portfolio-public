from django.db import models
from projects.models import slug_generator
from django.db.models.signals import pre_save

# Create your models here.


class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True, default=None)
    icon = models.CharField(max_length=50, blank=True)
    navbar_display = models.BooleanField(default=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)
    in_html = models.CharField(max_length=150, blank=True)
    SKILL_LEVEL_CHOICES = [('OWNED', 'Owned'), ('FAMILIAR', 'Familiar'), ('FUTURE', 'Future')]
    level = models.CharField(max_length=10, choices=SKILL_LEVEL_CHOICES, default='FUTURE')


def in_html_generator(sender, instance, *args, **kwargs):
    instance.in_html = '<li>'+instance.name+'</li>'


pre_save.connect(slug_generator, sender=Page)
pre_save.connect(in_html_generator, sender=Skill)
