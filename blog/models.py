from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date


class BlogPost(models.Model):
    title = models.CharField(max_length=254)
    body = models.TextField()
    image = models.ImageField(blank=True)
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts', blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title
