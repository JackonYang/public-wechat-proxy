# -*- coding: utf-8 -*-
from django.conf.urls import url, include
# from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^heartbeat/', include('heartbeat.urls')),
]
