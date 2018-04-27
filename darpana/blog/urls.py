from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('add', views.add_content, name='add_content'),
    path('delete', views.delete_content, name='delete_content'),
]
