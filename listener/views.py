# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from wechatpy import parse_message
from wechatpy.replies import TextReply


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
    income_msg = parse_message(request.body)
    print income_msg
    reply_text = 'welcome'
    reply = TextReply(content=reply_text, message=income_msg)
    reply_xml = reply.render()
    return HttpResponse(reply_xml)
