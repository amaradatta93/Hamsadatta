import pprint

from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render

from blog.models import Category, BlogPost


def view_all_blog_post(request):
    posts = BlogPost.objects.values('title', 'pk')
    return render(request, 'main_page.html', {'posts': posts})


def view_category(request):
    # categories = get_object_or_404(Category, pk=category_id)
    categories = Category.objects.values('name')
    pprint.pprint(categories)
    for i in categories:
        print(i)
    return HttpResponse(categories)
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
    post_content = get_object_or_404(BlogPost, pk=blog_id)
    return render(request, 'content.html', {"contents": post_content.as_dict()})

