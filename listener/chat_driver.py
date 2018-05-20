# -*- coding:utf-8 -*-
import json
import requests

from settings import CHAT_SERVER_URL


MSG_TMPL = {
    'msg_type': 'text',
    'msg_text': 'hello, fake message',
    'sender_puid': 'sender_puid',
    'sender_name': 'sender_name',
    'member_puid': 'member_puid',
    'member_name': 'member_name',
}

headers = {
    "Content-Type": "application/json; charset=utf-8",
}


def abstract_personal_msg(msg):
    return {
        'msg_type': msg.type,
        'msg_text': msg.text,
        'sender_puid': msg.sender.puid,
        'sender_name': msg.sender.name,
        'member_puid': msg.member and msg.member.puid,
        'member_name': msg.member and msg.member.name,
    }


def abstract_public_msg(msg):
    return {
        'msg_type': msg.type,
        'msg_text': msg.content,
        'sender_puid': msg.source,
        'sender_name': '-',
        'member_puid': '-',
        'member_name': '-',
    }


def send_msg(msg_source, msg_body):

    handlers = {
        'fake': lambda x: x,
        'wechat_personal': abstract_personal_msg,
        'wechat_public': abstract_public_msg,
    }

    data = handlers[msg_source](msg_body)
    data['msg_source'] = msg_source

    rsp = requests.post(
        CHAT_SERVER_URL,
        headers=headers,
        data=json.dumps(data))

    return rsp


if __name__ == '__main__':
    rsp = send_msg('fake', MSG_TMPL)
    print rsp.json()
