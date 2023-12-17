from django.db import models

class Lesson(models.Model):
    day = models.CharField(max_length=100)
    time = models.CharField()
    subject = models.CharField(max_length=100)
    room = models.CharField(max_length=20)
    description = models.TextField()
