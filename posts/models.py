from django.db import models
from users.models import CustomUser
from django.db.models import Q

class Status(models.TextChoices):
    DR = 'draft', 'DRAFT',
    PB = 'published', 'Published',


class CustomManager(models.Manager):
    def for_user(self, user):
        return super().get_queryset().filter(author = user)
    def search(self, user,q):
        p =  self.filter(
            Q(title__icontains=q) |
            Q(created__icontains=q) |
            Q(publish__icontains=q)
        )
        p.filter(author = user)
        return p

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    publish = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(default=Status.DR, choices=Status, max_length=10)


    objects = CustomManager()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "contact"
        ordering = ["-created"]