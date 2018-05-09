from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'blog'

urlpatterns = [
    path('add_content', TemplateView.as_view(template_name='add_post.html'), name='add_post'),
    path('edit_content', views.edit_content, name='add_content'),
    path('delete_delete', views.delete_content, name='delete_content'),
    path('add_category', views.add_category, name='add_content'),
    path('edit_category', views.edit_category, name='add_content'),
    path('delete_category', views.delete_category, name='delete_content'),
]
