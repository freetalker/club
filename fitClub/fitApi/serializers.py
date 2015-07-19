# coding=utf-8

from django.forms import widgets
from rest_framework import serializers
from fitHealth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','loginname','nickname','realname')

