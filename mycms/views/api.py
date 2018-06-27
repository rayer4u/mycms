# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from collections import OrderedDict
from django.contrib.auth import get_user_model, login
from django.shortcuts import get_object_or_404, render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets, views
from rest_framework.exceptions import PermissionDenied
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import list_route
from aldryn_newsblog.models import Article
from aldryn_categories.models import Category
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .. import serializers
from .. import filters

UserModel = get_user_model()


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UserSerializer
    queryset = UserModel.objects.all()


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    # serializer_class = serializers.ArticleSerializer
    queryset = Article.objects.published()
    filter_backends = (DjangoFilterBackend,)
    filter_class = filters.ArticleFilter
    # filter_fields = ('categories', 'tags')

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ArticleListSerializer
        return serializers.ArticleSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all()


class MyObtainAuthSession(ObtainAuthToken):
    login_success_response = openapi.Response('获取会话id成功', openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties=OrderedDict((
            ('sessionid', openapi.Schema(type=openapi.TYPE_STRING)),
        )),
        required=['sessionid']
    ))

    @swagger_auto_schema(operation_description="登录，获取session id",
                         query_serializer=AuthTokenSerializer,
                         responses={200: login_success_response})
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({'sessionid': request.session.session_key})
