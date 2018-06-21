from __future__ import absolute_import, print_function, unicode_literals

import pickle
from collections import OrderedDict

from cms.models import CMSPlugin, Page, Placeholder
from cms.utils.plugins import build_plugin_tree, downcast_plugins
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.urlresolvers import reverse
from django.db import models
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from rest_framework import serializers
from aldryn_newsblog.models import Article
from aldryn_categories.models import Category

from .utils import RequestSerializer

UserModel = get_user_model()


# class TagSerializerField(serializers.ListField):
#     child = serializers.CharField()

#     def to_representation(self, data):
#         return data.values_list('name', flat=True)


# class TagSerializer(serializers.ModelSerializer):
#     tags = TagSerializerField()

#     def create(self, validated_data):
#         tags = validated_data.pop('tags')
#         instance = super(TagSerializer, self).create(validated_data)
#         instance.tags.set(*tags)
#         return instance


class NormalSerializer(serializers.ModelSerializer):
    repr = serializers.SerializerMethodField()

    class Meta:
        fields = [
            'repr',
        ]

    def get_repr(self, obj):
        fields = []
        for f in obj._meta.get_fields():
            if f.related_model == f.model:
                continue
            value = getFieldValueOfObj(obj, f.name)

            fields.append((unicode(f), value))
        return fields


def getFieldValueOfObj(obj, name):
    # resolve picklists/choices, with get_xyz_display() function
    # return field.value_from_object(obj)
    get_choice = 'get_' + name + '_display'
    if hasattr(obj, get_choice):
        value = getattr(obj, get_choice)()
    else:
        try:
            value = getattr(obj, name)
        except AttributeError:
            value = None
    if value and not isinstance(value, unicode):
        if isinstance(value, str):
            value = value.decode('utf-8')
        else:
            try:
                value = unicode(value)
            except AttributeError:
                value = value.values_list('name', flat=True)
    return value


class UserSerializer(serializers.ModelSerializer):
    # articles = serializers.SerializerMethodField()

    class Meta:
        model = UserModel
        fields = [
            "id",
            # "password",
            "last_login",
            # "is_superuser",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_active",
            "date_joined",
            "groups",
            "user_permissions",
            # "articles",
        ]
        # depth = 1

    # def get_articles(self, obj):
    #     return getFieldValueOfObj(obj, 'article')


class ArticleSerializer(TaggitSerializer, RequestSerializer, serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    # owner = UserSerializer()
    tags = TagListSerializerField()
    title = serializers.SerializerMethodField()
    lead_in = serializers.SerializerMethodField()
    featured_image = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'
        # depth = 1

    def get_url(self, obj):
        return self.request.build_absolute_uri(obj.get_absolute_url())

    def get_title(self, obj):
        return obj.title

    def get_lead_in(self, obj):
        return obj.lead_in

    def get_featured_image(self, obj):
        if obj.featured_image:
            return self.request.build_absolute_uri(obj.featured_image.url)
        else:
            return None


class CategorySerializer(RequestSerializer, serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    slug = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_name(self, obj):
        return obj.name

    def get_slug(self, obj):
        return obj.slug
