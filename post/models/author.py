from django.db import models
class Author(models.Model):
    full_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return self.full_name