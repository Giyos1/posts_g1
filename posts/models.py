from django.db import models
from django.contrib.auth.models import User

class Status(models.TextChoices):
    DR = 'draft', 'DRAFT',
    PB = 'published', 'Published',

class Post(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(default=Status.DR, choices=Status, max_length=10)