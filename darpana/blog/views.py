from django.http import HttpResponse


def add_content(request):
    return HttpResponse('Hi add content here')


def delete_content(request):
    return HttpResponse('We will delete content here')
