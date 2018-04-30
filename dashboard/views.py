from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from blog.models import BlogPost


def content(request):
    # blog = BlogPost.objects.all()
    blog = get_object_or_404(BlogPost)
    return HttpResponse(blog)
