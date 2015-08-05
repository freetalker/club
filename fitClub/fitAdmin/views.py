# coding=utf-8

from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms import forms
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render_to_response

from models import *


@login_required(login_url='/login/')
def admin(req):
    now_str = timezone.now
    return render_to_response("fitAdmin/index.html", {'title': '首页', 'now': now_str})


@login_required(login_url='/login/')
def user_list(req):
    user_list = User.objects.all()
    paginator = Paginator(user_list, 10)

    page = req.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    page_start = (users.number - 1) * users.paginator.per_page + 1
    if users.has_next:
        page_end = users.number * users.paginator.per_page
    else:
        page_end = users.count

    return render_to_response("fitAdmin/user_list.html",
                              {'users': users, 'start': page_start, 'end': page_end, 'per': 11})


@login_required(login_url='/login/')
def product_list(req):
    data_list = Product.objects.all()
    paginator = Paginator(data_list, 10)

    page = req.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    page_start = (data.number - 1) * data.paginator.per_page + 1
    if data.has_next:
        page_end = data.number * data.paginator.per_page
    else:
        page_end = data.count

    return render_to_response("fitAdmin/product_list.html",
                              {'items': data, 'start': page_start, 'end': page_end, 'per': 21})


@login_required(login_url='/login/')
def orders_list(req):
    data_list = Order.objects.all()
    paginator = Paginator(data_list, 10)

    page = req.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    page_start = (data.number - 1) * data.paginator.per_page + 1
    if data.has_next:
        page_end = data.number * data.paginator.per_page
    else:
        page_end = data.count

    return render_to_response("fitAdmin/order_list.html",
                              {'items': data, 'start': page_start, 'end': page_end, 'per': 22})


@login_required(login_url='/login/')
def stat_user(req):

    from django.template.context_processors import csrf
    c = {}
    c.update(csrf(req))
    c['per'] = 31
    return render_to_response("fitAdmin/stat_user.html", c)


@login_required(login_url='/login/')
def stat_sport(req):
    return render_to_response("fitAdmin/stat_sport.html", {'per': 32})


@login_required(login_url='/login/')
def conf_base(req):
    return render_to_response("fitAdmin/conf_base.html", {'per': 41})


@login_required(login_url='/login/')
def conf_alarm(req):
    return render_to_response("fitAdmin/conf_alarm.html", {'per': 42})

class ImageUploadForm(forms.Form):
    image = forms.FileField()

def upload_file(req):
    if req.method == 'POST':
        form = ImageUploadForm(req.POST, req.FILES)  # 有文件上传要传如两个字段
        if form.is_valid():
            u = User.objects.get(pk = 1)
            u.avatar = form.cleaned_data['image']  # 直接在这里使用 字段名获取即可
            u.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')
