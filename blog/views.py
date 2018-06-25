from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Category, BlogPost


def view_content(request):
    posts = BlogPost.get_latest_by('title')
    JsonResponse({'posts': posts})


def view_category(request):
    # name_cat = list(Category.objects.filter(slug='asdfg'))
    name_cat = get_object_or_404(Category)
    print(name_cat)
    return JsonResponse(name_cat)
