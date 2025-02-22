from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.widgets import DateTimeInput

from posts.models import Post

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "slug"]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nomini kiriting!'}),
            'slug': forms.TextInput(attrs={'class': 'form-control',}),
        }