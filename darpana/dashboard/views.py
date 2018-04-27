from django.http import HttpResponse


def initial_hi(request):
    return HttpResponse('Hi my poems will come here')
