from django.conf.urls import url
from .views import *

'''
第一阶段
'''

urlpatterns = [
    #判断路径
    url(r'^', first_status)
]