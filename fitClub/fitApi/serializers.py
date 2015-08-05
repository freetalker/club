# coding=utf-8

from rest_framework import serializers
from fitAdmin.models import User

class UserSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(allow_null=True, required=False)
    realname = serializers.CharField(allow_null=True, required=False)
    sex = serializers.IntegerField(allow_null=True, required=False)
    remark = serializers.CharField(allow_blank=True, required=False)
    birthday = serializers.DateField(required=False)
    address = serializers.CharField(allow_blank=True,required=False)

    class Meta:
        model = User
        fields = ('id','loginname','nickname','realname','avatar','sex','address','birthday','remark','height','weight')
        read_only_fields = ('id','loginname','avatar')


class AvatarSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(use_url=True)

    class Meta:
        model = User
        fields = ('avatar',)