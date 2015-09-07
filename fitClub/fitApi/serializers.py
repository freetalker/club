# coding=utf-8

from rest_framework import serializers
from fitAdmin.models import *

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

class UserBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('nickname','realname','avatar','sex')

class AvatarSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(use_url=True)

    class Meta:
        model = User
        fields = ('avatar',)


class SportConfSerializer(serializers.ModelSerializer):
    points = serializers.IntegerField(required=False)
    steps = serializers.IntegerField(required=False)
    distances = serializers.FloatField(required=False)
    calories = serializers.FloatField(required=False)

    class Meta:
        model = SportConf
        fields = ('points','steps','distances','calories')

class SportStatSerializer(serializers.ModelSerializer):

    class Meta:
        model = SportStat
        fields = ('points','steps','distances','calories','last_time')

class SportDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = SportDate
        fields = ('points','steps','distances','calories','last_time','sport_date')

class SportDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = SportDetail
        fields = ('create_time','end_time','duration','type','points','steps','calories','distances')

class KnowledgeSerializer(serializers.ModelSerializer):
    cover = serializers.ImageField(source='cover_path')
    class Meta:
        model = Knowledge
        fields = ('id','create_time','title','cover','content','author')

class KnowledgeTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = KnowledgeType
        fields = ('id','name',)

