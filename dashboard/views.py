import json

from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from blog.models import BlogPost


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
        # blog_post.categories = body['categories']

        try:
            blog_post.save()
            messages.success(request, 'Saved the Post')
            return HttpResponse('Saved')
        except IntegrityError:
            messages.warning(request, 'Post already exists')
            return HttpResponse('Not saved')
    else:
        return HttpResponse("form not valid")
    # return redirect('/blog')


def edit_content(request):
    return HttpResponse('We will edit content here')


def delete_content(request):
    return HttpResponse('We will delete content here')


def add_category(request):
    return HttpResponse('We will add category here')


def edit_category(request):
    return HttpResponse('We will edit category here')


def delete_category(request):
    return HttpResponse('We will delete category here')
