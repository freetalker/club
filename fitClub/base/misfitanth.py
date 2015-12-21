# coding=utf-8

from misfit import Misfit
from misfit.auth import MisfitAuth

misfit_app_key = 'QaQCAfBPfDvQGQ6w'
misfit_app_secret = '4K5tcnsUnZiCidTGzJK1DQCJZdyriaDm'
misfit_redirect_uri='http://127.0.0.1:8000/misfit/auth'

def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

@singleton
class MisfitAuth(object):
    misfit = MisfitAuth(misfit_app_key, misfit_app_secret, misfit_redirect_uri)
    def __init__(self):
        print self.misfit