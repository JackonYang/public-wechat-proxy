# -*- coding:utf-8 -*-
import os


CHAT_SERVER_HOST = os.environ.get('CHAT_SERVER_HOST', '127.0.0.1')
CHAT_SERVER_PORT = os.environ.get('CHAT_SERVER_PORT', '6061')

CHAT_SERVER_URL = 'http://%s:%s/%s' % (
    CHAT_SERVER_HOST,
    CHAT_SERVER_PORT,
    'chat/',
)
