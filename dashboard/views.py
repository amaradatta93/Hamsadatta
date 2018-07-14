import json

from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from blog.models import BlogPost, Category


@csrf_exempt
def add_content(request):
    if request.method == "POST":

        body_unicode = request.body.decode(encoding='UTF-8')
        body = json.loads(body_unicode)

        blog_post = BlogPost()
        blog_post.title = body['title']
        blog_post.slug = body['slug']
        blog_post.content = body['content']
        blog_post.posted = body['posted']
        blog_post.language = body['language']

        try:
            blog_post.save()
        except IntegrityError:
            messages.warning(request, 'Post already exists')
            return HttpResponse('Not saved')
        try:
            for each_category in body['categories']:
                category_post = get_object_or_404(Category, name=each_category)
                print(category_post.name)
                blog_post.categories.add(category_post)
                blog_post.save()
                messages.success(request, 'Saved the Post')
                return HttpResponse('Saved')

        except:
            return HttpResponse('Undefined category')
    else:
        return HttpResponse("form not valid")
    # return redirect('/blog')


def edit_content(request):
    return HttpResponse('We will edit content here')


def delete_content(request):
    return HttpResponse('We will delete content here')


@csrf_exempt
def add_category(request):
    if request.method == "POST":
        body_unicode = request.body.decode(encoding='UTF-8')
        body = json.loads(body_unicode)

        category_post = Category()

        category_post.name = body['name']
        category_post.slug = body['slug']

        try:
            category_post.save()
            messages.success(request, 'Category Saved')
            return HttpResponse('Category saved')
        except IntegrityError:
            messages.warning(request, 'Category already exists')
            return HttpResponse('Category not saved')
    else:
        return HttpResponse("Form not valid")


def edit_category(request):
    return HttpResponse('We will edit category here')


def delete_category(request):
    return HttpResponse('We will delete category here')
