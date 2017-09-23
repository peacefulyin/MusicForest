# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect, render_to_response
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from django.core.paginator import Paginator
from django.conf import settings
from django.core.mail import send_mail

import random
from collections import defaultdict
from models import User,Sheet,Comment

import smtplib
from email.mime.text import MIMEText
from email.header import Header


def handler404(request):
    return render(request,'piano/404.html')


def index(request):
    context = defaultdict()
    try:
        if request.session['islogin'] == 'True':
            context['islogin'] = 'yes'
    except:
        context['islogin'] = 'no'

    sheet = Sheet.objects.values('album').distinct().order_by('album')[0:42]
    paginator = Paginator(sheet,6)
    #pages = [{'page%s'%str(i):paginator.page(i)} for i in paginator.page_range]

    for i in paginator.page_range:
        context['sheet'+str(i)] = paginator.page(i)
    return render(request, 'piano/index.html' ,context)


@csrf_exempt
def list(request, title):
    sheets = Sheet.objects.filter(album=title)
    list = [{'music':x.music,'page_num':x.page_num, 'album':x.album} for x in sheets]
    sample = random.sample(xrange(Sheet.objects.count()), 4)
    recommend = [{'music':Sheet.objects.all()[i].music,'page_num':Sheet.objects.all()[i].page_num, 'album':Sheet.objects.all()[i].album} for i in sample]
    print recommend
    return JsonResponse({'list':list,'recommend':recommend})


def show_sheet(request, name):
    sheet = Sheet.objects.get(music=name)
    for_list = [x+1 for x in range(sheet.page_num)]
    context = {'sheet':sheet,'for_list':for_list}
    return render(request,'piano/sheet.html',context)


def category(request, name):
    response = HttpResponse()
    sheets = Sheet.objects.values('album').distinct().order_by('album')
    len_sheet = len(sheets)
    quarter = len_sheet/4
    sheet = ''
    if name == 'new':
        sheet = sheets[:quarter]
    elif name == 'hot':
        sheet = sheets[quarter:quarter*2]
    elif name == 'treasure':
        sheet = sheets[quarter*2:quarter*3]
    elif name == 'like':
        sheet = sheets[quarter*3:]
    elif name == 'all':
        sheet = sheets
    context = {'sheet':sheet}
    return render(request, 'piano/list.html', context)


@csrf_exempt
def signin(request):
    name = request.POST.get('name')
    password = request.POST.get('password')
    print (name,password)
    if '@' in name:
        try:
            user = User.objects.get(email=name)
        except:
            user = None
    else:
        try:
            user = User.objects.get(uname=name)
        except:
            user = None
    if not user:
        return JsonResponse({'wrong':'用户名或邮箱错误'})
    truepwd = user.upwd
    if password != truepwd:
        return  JsonResponse({'wrong':'密码错误'})
    request.session['islogin'] = 'True'
    response = JsonResponse({'true': '登录成功'})
    response.set_cookie('islogin','True')
    return response


@csrf_exempt
def signup(request):
    username = request.POST.get('upname')
    email = request.POST.get('upemail')
    password = request.POST.get('uppassword')
    if username and email and password:
        user = User()
        user.uname = username
        user.upwd = password
        user.email = email
        try:
            user.save()
        except:
            return HttpResponse('错误，请重试')
    request.session['signup'] = 'success'
    return redirect('/home')


def quitlogin(request):
    request.session['islogin'] = 'False'
    return JsonResponse({'true': '退出登录成功'})


def findpass(requst, name):
    if '@' in name:
        try:
            user = User.objects.get(email=name)
        except:
            user = None
    else:
        try:
            user = User.objects.get(uname=name)
        except:
            user = None
    if not user:
        return JsonResponse({'wrong':'用户名或邮箱错误'})
    email = user.email

    """
    _user = '731769168@qq.com'
    _pwd = 'JohnSnow@321'
    _to = "1348032487@qq.com"
    
    msg = MIMEText('hello','utf-8')
    msg["Subject"] = "don't panic"
    msg["From"] = _user
    msg["To"] = _to
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())
    s.quit()
    """
    return JsonResponse({'true':email})














