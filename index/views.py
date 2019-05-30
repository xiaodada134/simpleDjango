from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'GET':
        addr = request.META['HTTP_REFERER']
        resp0 = render(request, 'login.html')
        resp0.set_cookie('L_cookie', addr, 60 * 60 )

        return resp0

    info = request.POST
    name = info.get('loginName')
    password = info.get('password')
    print(name, password)
    obj = Users.objects.get(uname=name)
    pwd = obj.upwd
    if pwd == password:
        # 记录session
        request.session['name'] = name
        addr1 = request.COOKIES.get('L_cookie', '')
        # 返回源地址
        resp = redirect(addr1)
        resp.set_cookie('name', name, 60*60*60)
        resp.delete_cookie('L_cookie')
        return resp
    else:
        err = '用户名或密码错误'
        return render(request, 'login.html', locals())

# 处理推出逻辑
def quit(request):
    pass

def err(request):
    return HttpResponse("页面not found, 请前往首页面<p><a href='http://172.88.10.156:8000/'>首页</a></p>")