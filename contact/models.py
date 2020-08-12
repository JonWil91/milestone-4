from django.db import models


class Contact(models.Model):

    class Meta:
        verbose_name_plural = 'Contact'

    name = models.CharField(max_length=50)
    email = models.EmailField()
    message_title = models.CharField(max_length=100, default="message_title")
    message = models.TextField()

    def __str__(self):
        return self.message_title
