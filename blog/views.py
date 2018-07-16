import pprint

from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404

from .models import Category, BlogPost


def view_title_category(request):
    # posts = BlogPost.objects.all()
    # post_contents = list(posts.values('title', 'slug'))
    # for values in post_contents:
    #     print(values)
    # return post_contents
    # posts = get_object_or_404(BlogPost, 'title')
    posts = BlogPost.objects.values('title')
    # titles = list(pos)
    pprint.pprint(posts)
    for i in posts:
        print(i)
    return HttpResponse(posts)


def view_category(request, category_id):
    categories = get_object_or_404(Category, pk=category_id)
    return JsonResponse(categories.as_dict())
    # categories = Category.objects.all()
    # categories_content = categories.values('name')
    # category_name = []
    # # print(categories_content)
    # for values in categories_content:
    #     # print(values)
    #     # print(values['name'])
    #     category_name += [values['name']]
    # print(category_name)
    # return category_name


def view_content(request, blog_id):
    posts = get_object_or_404(BlogPost, pk=blog_id)
    pprint.pprint(posts.content)
    return JsonResponse(posts.as_dict())
    # return post_contents
