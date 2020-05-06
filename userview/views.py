from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from blog.models import BlogPost, Category


@csrf_exempt
def view_all_blog_post(request):
    posts = list(BlogPost.objects.values('title', 'pk', 'image'))
    return JsonResponse({'posts': posts})


@csrf_exempt
def view_categories_blog_post(request, category_id):
    posts = list(BlogPost.objects.filter(categories=category_id).values('title', 'pk', 'image'))
    if posts:
        return JsonResponse({'posts': posts})
    else:
        return JsonResponse({'errors': 'No post in this category yet'})


@csrf_exempt
def view_search_blog_post(request):
    search_param = request.GET.get('search_param')
    posts = BlogPost.objects.filter(slug__contains=search_param)
    if posts:
        return JsonResponse({'posts': posts})
    else:
        return JsonResponse({'errors': 'Search result not found'})


@csrf_exempt
def view_content(request, blog_id):
    post_content = get_object_or_404(BlogPost, pk=blog_id)
    return JsonResponse({"contents": post_content.as_dict()})


@csrf_exempt
def return_category_details(request):
    categories = list(Category.objects.values('name', 'pk'))
    return JsonResponse({'categories': categories})
