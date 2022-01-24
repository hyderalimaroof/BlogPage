from django.db import models
from django.utils import timezone

class Posts (models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
