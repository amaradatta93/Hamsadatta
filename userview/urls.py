from django.urls import path

from . import views

app_name = 'userview'

urlpatterns = [
    path('posts', views.view_all_blog_post, name='posts'),
    path('posts/<int:blog_id>', views.view_content, name='each_post'),
    path('category/', views.return_category_details, name='category'),
    path('categories/<int:category_id>', views.view_categories_blog_post, name='categories'),
    path('search', views.view_search_blog_post, name='search'),
]
