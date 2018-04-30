from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('add', views.add_content, name='add_content'),
    path('delete', views.delete_content, name='delete_content'),
]
