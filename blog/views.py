from django.http import JsonResponse

from .models import Category


def view_content(request):
    pass


def view_category(request):
    categories = Category.objects.all()
    JsonResponse(request, {categories: 'categories'})
