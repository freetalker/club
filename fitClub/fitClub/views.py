# coding=utf-8
import datetime
import json
from django.forms import forms
from django.http import HttpResponse
from django.template import Template, RequestContext
from django.shortcuts import render_to_response
from misfit import Misfit
from misfit.auth import MisfitAuth

misfit_app_key = 'QaQCAfBPfDvQGQ6w'
misfit_app_secret = '4K5tcnsUnZiCidTGzJK1DQCJZdyriaDm'

def hello(req):
    return HttpResponse("hello world")

def home(req):
    now = datetime.datetime.now()
    t = r'首页'

    return render_to_response("fitHealth/index.html",{'t':t,'current_title':now})

def misfit(req):
    if req.method == 'GET':
        return render_to_response('fitClub/index.html',{'t':"dddd",'current_title':'now'})
    else:
        auth = MisfitAuth(misfit_app_key,misfit_app_secret,redirect_uri = 'http://fitclub.lyjohn.com/misfit/auth')
        auth_url = auth.authorize_url()

        response_data = {}
        response_data['url'] = auth_url
        return HttpResponse(json.dumps(response_data), content_type="application/json")

def misfit_authrize(req):
    if req.method == 'GET':
        auth = MisfitAuth(misfit_app_key,misfit_app_secret,redirect_uri = 'http://fitclub.lyjohn.com/misfit/auth')
        try:
            code = req.GET['code']
        except KeyError:
            return HttpResponse('code 必须有')

        try:
            state = req.GET['state']
        except KeyError:
            return  HttpResponse('state 必须有')

        access_token = auth.fetch_token(code, state)
        print  access_token

        misfit = Misfit(misfit_app_key, misfit_app_secret, access_token)
        print misfit.profile()

        return HttpResponse('Ok')
    else:
        return HttpResponse('Post 没用')