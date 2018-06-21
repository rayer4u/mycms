# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from rest_framework import pagination


class MyCursorPagination(pagination.PageNumberPagination):
    pass
    # ordering = 'id'
