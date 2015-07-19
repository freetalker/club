#coding=utf-8

from settings import *

DEBUG = False
TEMPLATE_DEBUG = False

# 设置邮箱地址，dj Project 出错时，发邮件通知
EMAIL_SUBJECT_PREFIX = '[django][mydj]'
EMAIL_HOST = 'localhost'

ADMINS = (
    ('John Ly', 'lyjohn@163.com'),
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fitclub',
        'USER': 'fitclub',
        'PASSWORD': 'abcd-1234',
        'HOST': '101.200.73.94',
        'PORT': '3306',
        'TIME_ZONE': 'Asia/Shanghai'
    }
}

SEND_BROKEN_LINK_EMAILS = True
MANAGERS = ADMINS
