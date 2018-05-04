from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.view_content, name='posts'),
    path('category', views.view_category, name='poems'),
]
