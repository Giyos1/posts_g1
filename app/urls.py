from django.contrib import admin
from django.urls import path
from app import views
app_name = 'app'
urlpatterns = [
    path('home/', views.home, name='home')
]