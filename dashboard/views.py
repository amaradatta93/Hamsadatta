from django.shortcuts import get_object_or_404, render

from blog.models import BlogPost


def view_all_blog_post(request):
    posts = BlogPost.objects.values('title', 'pk', 'image')
    return render(request, 'main_page.html', {'posts': posts})


def view_categories_blog_post(request, category_id):
    posts = BlogPost.objects.filter(categories=category_id)
    if posts:
        return render(request, 'main_page.html', {'posts': posts})
    else:
        return render(request, 'main_page.html', {'errors': 'No post in this category yet'})


def view_search_blog_post(request):
    search_param = request.GET.get('search_param')
    posts = BlogPost.objects.filter(slug__contains=search_param)
    if posts:
        return render(request, 'main_page.html', {'posts': posts})
    else:
        return render(request, 'main_page.html', {'errors': 'Search result not found'})


def view_content(request, blog_id):
    post_content = get_object_or_404(BlogPost, pk=blog_id)
    return render(request, 'content.html', {"contents": post_content.as_dict()})
