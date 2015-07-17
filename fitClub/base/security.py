# coding=utf-8
from pyDes import *
import base64
import hashlib
import types
import time

des_Key = 'FitClub0' # Key
des_IV = '\x08\x02\x07\x07\x01\x05\x01\x05' # IV向量
k = des(des_Key, CBC, des_IV, pad=None, padmode=PAD_PKCS5)

def desEncrypt(data):
    src = unicode.encode(data)
    EncryptStr = k.encrypt(src)

    return base64.b64encode(EncryptStr) #转base64编码返回

def desDecrypt(data):
    try: #base64解码 失败则不解码
        src = base64.decodestring(data)
    except:
        return ''

    return k.decrypt(src)

def md5(str):
    if type(str) is types.StringType:
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()
    else:
        return ''

def tokenGenerate(dict):
    var_id = str(dict['id'])
    var_name = dict['name']
    var_time = str(time.time())
    token = desEncrypt(var_id+","+var_name+","+var_time)

    return token

def tokenParse(data):
    token = desDecrypt(data)
    tmp =  token.split(',')

    return {"id":tmp[0],"name":tmp[1],"time":tmp[2]}