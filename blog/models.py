from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=254)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
