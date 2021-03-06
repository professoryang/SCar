import hashlib
import json
import logging

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from carapp import forms
from carapp.models import *


def index(request):
    brands = Brand.objects.all().values()
    outers = Outer.objects.all().values()
    return render(request, 'login/index.html',
                  {"brands": brands, "outers": outers})


def registe(request, models=None):
    if request.method == 'POST':
        print(request.FILES)
        registe_form = forms.RegisteForm(request.POST, request.FILES)
        message = "请检查填写的内容"
        if registe_form.is_valid():
            name = registe_form.cleaned_data['username']
            passwd = registe_form.cleaned_data['passwd']
            passwd2 = registe_form.cleaned_data['passwd2']
            email = registe_form.cleaned_data['email']
            phone = registe_form.cleaned_data['phone']
            img = registe_form.cleaned_data['img']
            if passwd != passwd2:
                message = "两次输入的密码不同"
                return render(request, 'login/registe.html', locals())
            else:
                same_name_user = User.objects.filter(name=name)
                if same_name_user:
                    message = "用户已经存在，请重新选择"
                    return render(request, 'login/registe.html', locals())
                same_email_user = User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/registe.html', locals())

            user1 = User()
            user1.name = name
            user1.passwd = protect(passwd)
            user1.passwd2 = passwd2
            user1.email = email
            user1.phone = phone
            user1.img = img
            user1.save()
            return redirect('/car/login/')
        else:
            message = registe_form.errors
    else:
        registe_form = forms.RegisteForm()
    return render(request, 'login/registe.html', locals())


def login(request):
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "请检查填写的内容！"

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(name=username)
                if user.passwd == protect(password):
                    # add session key: is_login, user_id, user_name
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/car/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def protect(obj):
    m = hashlib.md5()
    m.update(str(obj).encode())
    return m.hexdigest()


def logout(request):
    if not request.session.get('is_login'):
        return redirect('/car/index/')
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect('/car/index/')


def buycar(request):
    # 打印日志
    logging.getLogger('mdjango').warning('正在点击字母')
    letters = Letter.objects.all().values()
    t = []
    for i in letters:
        t.append(i['name'])
    brands = Brand.objects.all().values()
    return render(request, 'car/buycar.html', {'letters': t, 'brands': brands})


def buycarone(request):
    lett = request.GET.get('lett')
    letters = Letter.objects.get(name=lett).pinpai_set.all().values()
    print(type(letters))

    return HttpResponse(json.dumps(list(letters)))
