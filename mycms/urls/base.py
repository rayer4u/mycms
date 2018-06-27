# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import registration.backends.hmac.urls
from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .. import views
from .api import router


api_info = openapi.Info(
    title="开放api",
    default_version='v1',
    description="网站开放访问内容的api",
    terms_of_service="",
    contact=openapi.Contact(email="someone@someplace.local"),
    # license=openapi.License(name="BSD License"),
)

schema_view = get_schema_view(
    info=api_info,
    validators=['flex'],  # , 'ssv'],
    public=True,
    # permission_classes=(permissions.AllowAny,),
)

admin.autodiscover()

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}}),
    # url('^', include('django.contrib.auth.urls')),
    url(r'^accounts/login/$',
        views.LoginView.as_view(),
        name='auth_login'),
    url(r'^accounts/register/$',
        views.RegistrationView.as_view(),
        name='registration_register'),  # 定制界面用
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    # url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^api/session/$', views.MyObtainAuthSession.as_view()),
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=None), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
]

urlpatterns += i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^', include('cms.urls')),
    prefix_default_language=False
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    ] + staticfiles_urlpatterns() + urlpatterns
