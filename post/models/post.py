from django.db import models
from .author import Author


class Status(models.TextChoices):
    DRAFT = 'DF', 'Draft'
    PUBLISHED = 'PB', 'Published'

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Status.PUBLISHED)

class Post(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=Status)
    published = PublishedManager()

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        db_table = 'post'

