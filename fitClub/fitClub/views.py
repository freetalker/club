# coding=utf-8
import datetime
import json
import logging
from django import forms
from django.http import HttpResponse
from django.template import Template, RequestContext
from django.shortcuts import render_to_response

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib import auth

# from misfit import Misfit
# from misfit.auth import MisfitAuth
# from misfit.notification import MisfitNotification
import simplejson as simplejson

from fitAdmin.models import *
from base.misfitanth import *


class LoginForm(forms.Form):
    loginname = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)


def hello(req):
    return HttpResponse("hello world")


def home(req):
    now = datetime.datetime.now()

    return render_to_response("fitClub/index.html", {'title': '首页', 'current_time': now})


def login(req):
    if req.method == 'POST':
        uf = LoginForm(req.POST)
        if (uf.is_valid()):
            # 获得表单数据
            username = uf.cleaned_data['loginname']
            password = uf.cleaned_data['password']

            result = {"status": False, "data": ""}
            if username == "" or username.isspace():
                result = {"status": False, "data": "用户名不能为空"}
                return HttpResponse(simplejson.dumps(result, ensure_ascii=False), content_type="application/json")
            if password == "" or password.isspace():
                result = {"status": False, "data": "密码不能为空"}
                return HttpResponse(simplejson.dumps(result, ensure_ascii=False), content_type="application/json")

        user = auth.authenticate(loginname=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(req, user)
                result = {"status": True, "data": "OK"}
                return HttpResponse(simplejson.dumps(result, ensure_ascii=False), content_type="application/json")
            else:
                result = {"status": False, "data": "[" + username + "]已被暂时禁用"}
                return HttpResponse(simplejson.dumps(result, ensure_ascii=False), content_type="application/json")
        else:
            result = {"status": False, "data": "用户名或密码不正确，请重试"}
            return HttpResponse(simplejson.dumps(result, ensure_ascii=False), content_type="application/json")
    else:
        return render_to_response("fitClub/index.html", {'title': '登录系统'})

def error(req, code):
    return render_to_response("fitClub/error-" + code + ".html");


# misfitAuth = MisfitAuth(misfit_app_key, misfit_app_secret, redirect_uri='http://127.0.0.1:8000/misfit/auth')
# print misfitAuth
#
#
def misfit(req):
    if req.method == 'GET':
        now = datetime.datetime.now()
        return render_to_response('fitClub/misfit.html', {'title': r'绑定Misfit'})
    else:
        auth = MisfitAuth().misfit

        auth_url = auth.authorize_url()

        response_data = {}
        response_data['url'] = auth_url
        return HttpResponse(json.dumps(response_data), content_type="application/json")


def misfit_authrize(req):
    if req.method == 'GET':
        try:
            code = req.GET['code']
        except KeyError:
            return HttpResponse('code 必须有')

        try:
            state = req.GET['state']
        except KeyError:
            return HttpResponse('state 必须有')

        log = logging.getLogger('misfit')

        access_token = MisfitAuth().misfit.fetch_token(code, state)
        log.info(access_token)
        misfit = Misfit(misfit_app_key, misfit_app_secret, access_token)
        log.info(r"用户ID：" + misfit.profile().userId)
        print misfit.profile()
        print misfit.device()
        print misfit.goal()
        print misfit.summary()

        return HttpResponse('Ok')
    else:
        return HttpResponse('Post 没用')

#
# def misfit_notification(req):
#     if req.method == 'POST':
#         log = logging.getLogger('misfit')
#
#         log.error(req.body)
#         tt = '''{"Type":"SubscriptionConfirmation","Token":"9be2bb3091de2e7fead174e956c2a37671ea8fc327b8bad2c7787666dcdc3b1683933a58549075330ee7d3e02d28166e4c0f2fa0069dcd8585c1354918d71d81bcd1547ee340f7c49445eb8333bbe8baf01fc2fcd39d5c217ad27063e9bcc8c15c71b2607ea654b02c8acff6176718d3163784ff13a113ba638982814a1d85ccf4c86fdc5f81155318ab7250b5b526a1","TopicArn":"arn:aws:sns:us-east-1:819895241319:test","Message":"You have chosen to subscribe to the topic arn:aws:sns:us-east-1:819895241319:test.\nTo confirm the subscription, visit the SubscribeURL included in this message.","SubscribeURL":"https://build.misfit.com/apps/554dcf3cbf1f69944e599eed/verify_endpoint?verify_token=$2a$10$ellHichPxhKfNOgfNTWwGeYN2Y7AskSaw5WaF.dNIY1nPmvxggB3a&challenge=ca0697846a76a417","Timestamp":"2015-07-20T08:44:49.236Z"}''';
#         # notification = MisfitNotification(req.body)
#         log.error(tt)
#         notification = MisfitNotification(tt)
#         if notification.Type == 'Notification':
#             for message in notification.Message:
#                 log.info(message['type'])
#                 if message['type'] == 'goals':
#                     log.info(message['updatedAt'])
#                 elif message['type'] == 'profiles':
#                     log.info(message['action'] + message['updatedAt'])
#                 elif message['type'] == 'devices':
#                     log.info(message['action'] + message['updatedAt'])
#                 else:
#                     log.info(message['action'] + message['updatedAt'])
#         elif notification.Type == 'SubscriptionConfirmation':
#             log.info(notification.Type + notification.Message)
#         else:
#             log.info(r"未做处理")
#         return HttpResponse('')
#     else:  # GET
#         return render_to_response('fitClub/notification.html', {'title': 'MISFIT绑定'})
