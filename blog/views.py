from django.http import HttpResponse
from django.shortcuts import redirect

from .forms import BlogForm
from .models import BlogPost


def add_content(request):
    if request.method == "POST":
        blog_post_form = BlogForm(request.POST)

        if blog_post_form.is_valid():
            blog_post = BlogPost()
            blog_post.title = blog_post_form.cleaned_data['title']
            blog_post.slug = blog_post_form.cleaned_data['slug']
            blog_post.content = blog_post_form.cleaned_data['content']
            blog_post.posted = blog_post_form.cleaned_data['posted']
            blog_post.language = blog_post_form.cleaned_data['language']
            blog_post.category = blog_post_form.cleaned_data['category']
            blog_post.save()
    return redirect('/')


def delete_content(request):
    return HttpResponse('We will delete content here')
