from django.db import models
from datetime import datetime

# Create your models here.


class Message(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=250, blank=True)
    email = models.CharField(max_length=200)
    text = models.TextField()
    is_answered = models.BooleanField(default=False)
    contact_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
