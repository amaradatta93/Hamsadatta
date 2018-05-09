from django.shortcuts import render

from blog.models import Category


def view_content(request):
    pass


def view_category(request):
    categories = Category.objects.all()
    return render(request, 'dashboard.html', {'categories': categories})
