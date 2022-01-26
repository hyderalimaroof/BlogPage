from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post (models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    