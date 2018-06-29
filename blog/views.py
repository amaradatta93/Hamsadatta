from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import pprint


from .models import Category, BlogPost


def view_content(request):
    posts = BlogPost.objects.all()
    post_contents = list(posts.values('title', 'slug'))
    # pprint.pprint(post_contents)
    for values in post_contents:
        print(values)
    # return post_contents


def view_category(request):
    # name_cat = list(Category.objects.filter(slug='asdfg'))
    # name_cat = get_object_or_404(Category)
    # print(name_cat)
    pass
