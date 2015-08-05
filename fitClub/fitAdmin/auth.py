#coding=utf-8

'''
自定义登陆验证后台

Created on 2015年7月27日

@author: lyjohn
'''

import re
from fitAdmin.models import User
from django.conf import settings

class fitClubBackend:

    def authenticate(self, loginname=None, password=None):
        try:
            user = User.objects.get(loginname=loginname)
        except User.DoesNotExist:
            pass
        else:
            if user.check_password(password):
                return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None