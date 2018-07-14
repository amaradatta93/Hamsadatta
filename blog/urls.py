from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('posts', views.view_title_category, name='title'),
    path('category/<int:category_id>', views.view_category, name='view_category'),
    path('posts/<int:blog_id>', views.view_content, name='posts')
]
