# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import django_filters
from aldryn_newsblog.models import Article


class ArticleFilter(django_filters.FilterSet):
    # tag = django_filters.ModelChoiceFilter(
    #     name='tag', lookup_expr='isnull',
    #     null_label='Uncategorized',
    #     queryset=Category.objects.all(),
    # )
    # tags = django_filters.filters.CharFilter(method='filter_tag')

    # def filter_tag(request):
    #     if request is None:
    #         return Department.objects.none()

    #     company = request.user.company
    #     return company.department_set.all()

    class Meta:
        model = Article
        fields = ['categories']   # , 'tags']
        # filter_overrides =
