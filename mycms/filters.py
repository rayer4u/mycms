# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import django_filters
from aldryn_newsblog.models import Article


# 参考https://github.com/carltongibson/django-filter/issues/137
class ListFilter(django_filters.Filter):
    def filter(self, qs, value):
        if value not in django_filters.constants.EMPTY_VALUES:
            value_list = value.split(u',')
            return super(ListFilter, self).filter(qs, django_filters.fields.Lookup(value_list, 'in'))
        return super(ListFilter, self).filter(qs, value)


class ArticleFilter(django_filters.FilterSet):
    categories = ListFilter(name='categories__translations__slug')
    tags = ListFilter(name='tags__slug')

    class Meta:
        model = Article
        fields = ['categories', 'tags']
