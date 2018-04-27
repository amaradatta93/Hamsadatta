from django.http import HttpResponse


def content(request):
    return HttpResponse('Hi my poems will come here')
