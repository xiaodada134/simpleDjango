from django.shortcuts import render, redirect
from django.http import HttpResponse
from study import checkLoginStatus

# Create your views here.

def first_status(request):
    print(type(request))
    req = checkLoginStatus.Login_status(request)
    if not req.check():
        return redirect('/login')
    else:
        return redirect('http://naotu.baidu.com/file/afc394d7bd068a98734d3948275efe9b?token=c83a3f780c0eb681')