from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'posts'
urlpatterns = [
    path('', views.post_list, name = 'list'),
    path('detail/<int:id>/', views.post_detail, name = 'detail'),
    path('delete-post/<int:id>/', views.delete_post, name = 'delete-post'),

    path('edit-post/<int:id>/', views.edit_post, name='edit-post'),
    path('create/', views.create, name = 'create'),
]