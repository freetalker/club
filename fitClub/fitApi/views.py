# coding=utf-8
from datetime import datetime
import logging
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.security import *

from fitAdmin.models import User, SportConf
from fitApi.serializers import UserSerializer, AvatarSerializer, SportConfSerializer


@api_view(['GET', 'POST'])
def user_list(request, format=None):
    if request.method == 'GET':
        snippets = User.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk, format=None):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def user_login(request, format=None):
    if request.method == 'GET':
        return Response(status=status.HTTP_403_FORBIDDEN)

    elif request.method == 'POST':
        try:
            request.DATA['android']
            login_type = 2  # android
        except KeyError:
            login_type = 0
        if not login_type:
            try:
                request.DATA['ios']
                login_type = 3  # ios
            except KeyError:
                login_type = 1  # web

        # if login_type == 1:
        #     return Response({'status': 0, 'message': '需传输终端字段'})

        try:
            loginname = request.DATA['loginname']
        except KeyError:
            return Response({'status': 0, 'message': 'loginname 帐号必须填写'})

        try:
            password = request.DATA['password']
        except KeyError:
            return Response({'status': 0, 'message': 'password 密码必须填写'})

        users = User.objects.filter(loginname=loginname)

        if not users.exists():
            return Response({'status': 0, 'message': '用户不存在'})
        else:
            user = users.first()
            # Y9VtcSMp3KQ=  123456

            if login_type != 1:  # 不是web才加密 web直接登录了
                password = desDecrypt(password)
            else:
                password = str(password)

            if user.password != md5(password):
                return Response({'status': 0, 'message': '密码不正确'})
            elif not user.is_active:
                return Response({'status': 0, 'message': '用户已锁定'})
            else:
                if request.META.has_key('HTTP_X_FORWARDED_FOR'):
                    ip = request.META['HTTP_X_FORWARDED_FOR']
                else:
                    ip = request.META['REMOTE_ADDR']

                user.last_login_time = datetime.now()
                user.last_login_ip = ip
                user.last_login_type = login_type
                user.login()

                token = tokenGenerate({"id": user.id, "name": user.loginname})

                return Response({'status': 1, 'message': '登录成功', 'data': token})

@api_view(['GET','POST'])
def user_profile(request):
    try:
        token = request.GET['t']
    except KeyError:
        return Response({'status': 1, 'message': 'token值不存在'})

    log = logging.getLogger('common')

    token_data = tokenParse(token)

    if not token_data:
        return Response({'status': 1, 'message': 'token值不正确'})

    uid = token_data['id']

    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return Response({'status': 1, 'message': 'token解析不出来'})

    if request.method == 'GET':
        serializer = UserSerializer(user)

        return Response(dict(status=0, message='ok', data = serializer.data))

    elif request.method == 'POST':
        try:
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(dict(status=0, message = 'ok'))

            return Response(dict(status=1,message = serializer.errors))
        except Exception as exc:
            return Response(dict(status=1,message = exc.detail))

@api_view(['POST','GET'])
def user_avatar(request):
    try:
        token = request.GET['t']
    except KeyError:
        return Response({'status': 1, 'message': 'token值不存在'})

    token_data = tokenParse(token)

    if not token_data:
        return Response({'status': 1, 'message': 'token值不正确'})

    uid = token_data['id']

    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return Response(dict(status=1, message='token解析不出来'))

    if request.method == 'GET':
        serializer = AvatarSerializer(user)
        avatar = serializer.data['avatar']
        return Response(dict(status=0, message='ok', data=avatar))

    elif request.method == 'POST':
        try:
            serializer = AvatarSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                avatar = serializer.data['avatar']
                return Response(dict(status=0, message = 'ok',data=avatar))

            return Response(dict(status=1,message = serializer.errors))
        except Exception as exc:
            return Response(dict(status=1,message = exc.detail))


@api_view(['GET','POST'])
def user_profile(request):
    try:
        token = request.GET['t']
    except KeyError:
        return Response({'status': 1, 'message': 'token值不存在'})

    log = logging.getLogger('common')

    token_data = tokenParse(token)

    if not token_data:
        return Response({'status': 1, 'message': 'token值不正确'})

    uid = token_data['id']

    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return Response({'status': 1, 'message': 'token解析不出来'})

    if request.method == 'GET':
        serializer = UserSerializer(user)

        return Response(dict(status=0, message='ok', data = serializer.data))

    elif request.method == 'POST':
        try:
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(dict(status=0, message = 'ok'))

            return Response(dict(status=1,message = serializer.errors))
        except Exception as exc:
            return Response(dict(status=1,message = exc.detail))

@api_view(['POST','GET'])
def sport_conf(request):
    try:
        token = request.GET['t']
    except KeyError:
        return Response({'status': 1, 'message': 'token值不存在'})

    token_data = tokenParse(token)

    if not token_data:
        return Response({'status': 1, 'message': 'token值不正确'})

    uid = token_data['id']

    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return Response(dict(status=1, message='token解析不出来'))

    if request.method == 'GET':
        try:
            sportConf = user.sportconf
        except SportConf.DoesNotExist:
            return Response(dict(status=1,message='未设置目标'))

        serializer = SportConfSerializer(sportConf)
        return Response(dict(status=0, message='ok', data=serializer.data))

    elif request.method == 'POST':
        '''
        如果没有设置目标的话，可以通过POST创建目标，首先初始化一个
        '''
        try:
            sportConf = user.sportconf
        except SportConf.DoesNotExist:
            user.sportconf = SportConf()
            sportConf = user.sportconf

        try:
            serializer = SportConfSerializer(sportConf, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(dict(status=0, message = 'ok',data=serializer.data))

            return Response(dict(status=1,message = serializer.errors))
        except Exception as exc:
            return Response(dict(status=1,message = exc.detail))


