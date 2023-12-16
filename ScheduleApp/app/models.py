"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Schedule(models.Model):
    day = models.CharField(max_length=100)
    time = models.TimeField()
    subject = models.CharField(max_length=100)
    room = models.CharField(max_length=20)
    description = models.TextField()
    