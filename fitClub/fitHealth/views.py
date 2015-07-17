# coding=utf-8
from models import User,Member
from rest_framework import viewsets
from fitHealth.serializers import UserSerializer, MemberSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    允许查看和编辑user 的 API endpoint
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MemberViewSet(viewsets.ModelViewSet):
    """
    允许查看和编辑member的 API endpoint
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer