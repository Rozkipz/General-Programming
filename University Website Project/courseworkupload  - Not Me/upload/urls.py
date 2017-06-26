# -*- coding: utf-8 -*-
from django.conf.urls import url
from upload.views import upload


urlpatterns = [
    url(r'^upload/$', upload, name='upload')
]