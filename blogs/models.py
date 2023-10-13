from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft'),
    )

    title = models.CharField(max_length=100)
    text = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])
