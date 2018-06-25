# coding=UTF-8
from django.http import JsonResponse, HttpResponseRedirect
from hashlib import sha1

from django.shortcuts import render, redirect

# Create your views here.
from df_user.models import UserInfo


def register(request):
    context = {'title': '天天生鲜-注册'}
    return render(request, 'df_user/register.html', context)


def register_handler(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    ucpwd = post.get('cpwd')
    uemail = post.get('email')

    if upwd != ucpwd:
        return redirect('/user/register')
    s1 = sha1()
    s1.update(upwd.encode("utf8"))
    upwd3 = s1.hexdigest()

    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()

    return redirect('/user/login/')


def login(request):
    context = {'title': '天天生鲜-登录'}
    return render(request, 'df_user/login.html', context)


def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count': count})


def login_handler(request):
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    remember = post.get('remember')
    user = UserInfo.objects.filter(uname=uname)
    if len(user) == 1:
        s1 = sha1()
        s1.update(upwd.encode("utf8"))
        if s1.hexdigest() == user[0].upwd:
            red = HttpResponseRedirect('info')
            if remember != 0:
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname', '', max_age=-1)
            request.session['user_id'] = user[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1, 'uname': uname}
            return render(request, 'df_user/login.html', context)
    else:
        context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 0, 'uname': uname}
        return render(request, 'df_user/login.html', context)


def user_info(request):
    userInfo = UserInfo.objects.get(id=request.session['user_id'])
    context = {'title': '用户中心', 'uname': userInfo.uname, 'uemail': userInfo.uemail,'info':1}

    return render(request, 'df_user/user_center_info.html', context)


def user_site(request):
    userInfo = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        userInfo.uaddress = post.get('uaddress')
        userInfo.uyoubian = post.get('uyoubian')
        userInfo.uphone = post.get('uphone')
        userInfo.ushou = post.get('ushou')
        userInfo.save()
    context = {'title': '用户中心', 'user': userInfo,'site':1}

    return render(request, 'df_user/user_center_site.html', context)
