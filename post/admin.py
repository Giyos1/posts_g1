from django.contrib import admin
from .models.post import Post
from .models.author import Author

admin.site.register([Author, Post])
