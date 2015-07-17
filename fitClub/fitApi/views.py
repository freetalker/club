# coding=utf-8
from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.security import *

from fitHealth.models import User
from fitApi.serializers import UserSerializer

@api_view(['GET','POST'])
def user_list(request, format = None):
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

@api_view(['GET','PUT','DELETE'])
def user_detail(request, pk, format = None):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def user_login(request, format = None):
    if request.method == 'GET':
        return Response(status = status.HTTP_403_FORBIDDEN)

    elif request.method == 'POST':
        try:
            loginname = request.DATA['loginname']
        except KeyError:
            return Response({'status':0, 'message': 'loginname 帐号必须填写'})

        try:
            password = request.DATA['password']
        except KeyError:
            return Response({'status':0, 'message': 'password 密码必须填写'})

        users = User.objects.filter(loginname=loginname)

        if not users.exists():
            return Response({'status':0, 'message': '用户不存在'})
        else:
            user = users.first()
            # Y9VtcSMp3KQ=  123456

            password = desDecrypt(password)
            if user.password != md5(password):
                return Response({'status':0,'message': '密码不正确'})
            elif not user.is_active:
                return Response({'status':0,'message': '用户已锁定'})
            else:
                token = tokenGenerate({"id":user.id,"name":user.loginname})

                if request.META.has_key('HTTP_X_FORWARDED_FOR'):
                    ip =  request.META['HTTP_X_FORWARDED_FOR']
                else:
                    ip = request.META['REMOTE_ADDR']

                user.last_login_time = datetime.now()
                user.last_login_ip = ip

                try:
                    request.DATA['android']
                    login_type = 2 #android
                except KeyError:
                    login_type = 0
                if not login_type:
                    try:
                        request.DATA['ios']
                        login_type = 3 #ios
                    except KeyError:
                        login_type = 1 #web

                user.last_login_type = login_type
                user.login()

                return Response({'status':1,'message': '登录成功','token':token})
