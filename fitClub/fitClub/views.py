# coding=utf-8
import datetime
import json
import logging
from django.forms import forms
from django.http import HttpResponse
from django.template import Template, RequestContext
from django.shortcuts import render_to_response

from misfit.auth import MisfitAuth
from misfit.notification import MisfitNotification

misfit_app_key = 'QaQCAfBPfDvQGQ6w'
misfit_app_secret = '4K5tcnsUnZiCidTGzJK1DQCJZdyriaDm'

def hello(req):
    return HttpResponse("hello world")

def home(req):
    now = datetime.datetime.now()
    t = r'首页'

    return render_to_response("fitHealth/index.html",{'t':t,'current_title':now})

auth = MisfitAuth(misfit_app_key,misfit_app_secret,redirect_uri = 'http://127.0.0.1:8000/misfit/auth')
print auth
def misfit(req):
    if req.method == 'GET':
        now = datetime.datetime.now()
        return render_to_response('fitClub/index.html',{'t':r'绑定Misfit','current_title':now})
    else:
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
            return  HttpResponse('state 必须有')

        log = logging.getLogger('misfit')

        log.error(r'');
        access_token = auth.fetch_token(code, state)
        print access_token
        # misfit = Misfit(misfit_app_key, misfit_app_secret, access_token)
        # print misfit.profile()
        # print misfit.device()
        # print misfit.goal()
        # print misfit.summary()

        return HttpResponse('Ok')
    else:
        return HttpResponse('Post 没用')

def misfit_notification(req):
    if req.method == 'POST':
        notification = MisfitNotification(req.POST)
        if notification.type == 'Notification':
            log = logging.getLogger('misfit')
            for message in notification.Message:
                log.info(message['type'])
                if message['type'] == 'goals':
                    log.info(message['updatedAt'])
                elif message['type'] == 'profiles':
                    log.info(message['action']+message['updatedAt'])
                elif message['type'] == 'devices':
                    log.info(message['action']+message['updatedAt'])
                else:
                    log.info(message['action']+message['updatedAt'])
        elif notification.type == 'SubscriptionConfirmation':
            log = logging.getLogger('misfit')
            log.info(notification.type+notification.Message)
        else:
            log = logging.getLogger('misfit')
            log.info(r"未做处理")
        return HttpResponse('')
    else: #GET
        return HttpResponse(r'用作Notification响应')
