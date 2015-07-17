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

SEND_BROKEN_LINK_EMAILS = True
MANAGERS = ADMINS
