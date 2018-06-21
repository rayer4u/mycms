# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from rest_framework.routers import DefaultRouter
from .. import views

router = DefaultRouter(trailing_slash=False)
router.register(r'users', views.UserViewSet, 'user')
router.register(r'articles', views.ArticleViewSet, 'article')
router.register(r'categories', views.CategoryViewSet, 'category')
