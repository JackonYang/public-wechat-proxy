# -*- coding:utf-8 -*-
import os


CHAT_SERVER_HOST = os.environ.get('CHAT_SERVER_HOST', 'chat.10fen.jackon.me')
# CHAT_SERVER_PORT = os.environ.get('CHAT_SERVER_PORT', '6061')

CHAT_SERVER_URL = 'https://%s/%s' % (
    CHAT_SERVER_HOST,
    # CHAT_SERVER_PORT,
    'chat/',
)

print CHAT_SERVER_URL
