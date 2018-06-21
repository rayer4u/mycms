# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.contrib.auth import get_user_model, login
from rest_framework import mixins, viewsets, views
from rest_framework.exceptions import PermissionDenied
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import list_route
from django.shortcuts import get_object_or_404, render
from django_filters.rest_framework import DjangoFilterBackend
from aldryn_newsblog.models import Article
from aldryn_categories.models import Category

from .. import serializers
from .. import filters

UserModel = get_user_model()


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UserSerializer
    queryset = UserModel.objects.all()


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.ArticleSerializer
    queryset = Article.objects.published()
    filter_backends = (DjangoFilterBackend,)
    filter_class = filters.ArticleFilter
    # filter_fields = ('categories', 'tags')

    # def get_queryset(self):
    #     # project_id may be None
    #     return self.queryset \
    #         .filter(categories__translations__slug=self.kwargs.get('category')) \
    #         .filter(tags__slug=self.kwargs.get('tag'))

    def list(self, request, *args, **kwargs):
        # """
        # category -- A first parameter
        # tag -- A second parameter
        # """

        # queryset = self.queryset

        # category = request.query_params.get('category')
        # if (category):
        #     queryset = queryset.filter(categories__translations__slug=category)

        # tag = request.query_params.get('tag')
        # if (tag):
        #     queryset = queryset.filter(tags__slug=tag)

        # if (self.queryset != queryset):
        #     self.queryset = queryset

        return super(ArticleViewSet, self).list(request, args, kwargs)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all()


class MyObtainAuthSession(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({'sessionid': request.session.session_key})
