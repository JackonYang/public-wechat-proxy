# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def listening(request):
    if request.method == 'GET':
        return do_auth(request)
    elif request.method == 'POST':
        return reply_message(request)
    else:
        msg = 'Method "%s" not allowed.' % request.method
        return HttpResponse(msg, status=405)


def do_auth(request):
    echostr = request.GET.get('echostr')
    return HttpResponse(echostr, content_type="text/plain")


def reply_message(request):
    print(request.body)
    return HttpResponse('welcome')
