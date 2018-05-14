from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('add_post', views.add_content, name='add_post'),
    path('edit_post', views.edit_content, name='edit_post'),
    path('delete_post', views.delete_content, name='delete_post'),
    path('add_category', views.add_category, name='add_category'),
    path('edit_category', views.edit_category, name='edit_category'),
    path('delete_category', views.delete_category, name='delete_category'),
]
