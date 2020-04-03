from django.shortcuts import get_object_or_404, render

from blog.models import BlogPost


def view_all_blog_post(request):
    posts = BlogPost.objects.values('title', 'pk', 'image')
    return render(request, 'main_page.html', {'posts': posts})


def view_content(request, blog_id):
    post_content = get_object_or_404(BlogPost, pk=blog_id)
    return render(request, 'content.html', {"contents": post_content.as_dict()})
