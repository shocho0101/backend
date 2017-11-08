from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import authentication, permissions, generics
from rest_framework_jwt.settings import api_settings
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from django.db import transaction
from django.http import HttpResponse, Http404
from django_filters import filters

from rest_framework import status, viewsets, filters
from rest_framework.views import APIView

from .serializer import AccountSerializer, GroupListSerializer, GroupDetailSerializer
from .models import Account, AccountManager, Group
# Create your views here.

class AuthRegister(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def post(self, request, *args, **kwargs):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GroupList(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupListSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(member = request.user.id)
        serializer = GroupListSerializer(queryset, many= True)
        return Response(serializer.data)

class GroupDetail(APIView):
    def get(self, request, id):
        group = Group.objects.get(id = id)
        serializer = GroupDetailSerializer(group)
        return Response(serializer.data)

