"""darpana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from darpana import settings

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-dashboard/', include('dashboard.urls')),
    path('api/user-dashboard/', include('userview.urls')),
    path('blog/', include('blog.urls')),
    path('', TemplateView.as_view(template_name='index.html'))
] + static(settings.STATIC_URL)
