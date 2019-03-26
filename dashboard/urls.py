from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('posts', views.view_all_blog_post, name='title'),
    path('posts/<int:blog_id>', views.view_content, name='each_post')
]
