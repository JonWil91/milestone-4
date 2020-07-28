from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date


class BlogPost(models.Model):
    title = models.CharField(max_length=254)
    body = models.TextField()
    image = models.ImageField(blank=True)
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
