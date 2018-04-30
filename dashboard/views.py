from django.http import HttpResponse

from blog.models import BlogPost

def content(request):
    blog = BlogPost()
    return HttpResponse('Hi my poems will come here')
