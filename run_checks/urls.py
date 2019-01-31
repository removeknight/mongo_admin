from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('all_users/', views.all_users, name='all_users'),
    path('generate_users/', views.generate_users, name='generate_users'),
]