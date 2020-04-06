from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('add', views.BlogPostCreate.as_view(), name='add'),
    path('edit/<int:blog_id>', views.BlogPostUpdate.as_view(), name='edit'),
    path('delete/<int:blog_id>', views.BlogPostDelete.as_view(), name='delete'),
]
