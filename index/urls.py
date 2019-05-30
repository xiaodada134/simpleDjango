from django.conf.urls import url
from .views import *

urlpatterns = [
    #判断路径
    url(r'^index/$', index),
    url(r'^login',login),
    url(r'^$', index),
    url(r'^', err)
]