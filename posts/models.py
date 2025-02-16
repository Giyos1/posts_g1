from django.db import models

# Create your models here.

class Post(models.Model):
    class Status(models.TextChoices):
        DR = 'draft', 'Draft'
        PB = 'published', 'Published'
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=30)
    # author = models.ForeignKey(User)
    body = models.TextField(null=True, blank=True)
    published_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default=Status.DR, choices=Status.choices, max_length=20)



