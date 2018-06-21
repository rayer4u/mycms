# -*- coding: utf-8 -*-
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import LoginView as BaseLoginView
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from registration.backends.hmac.views import \
    RegistrationView as BaseRegistrationView

from ..forms import AuthenticationForm, RegistrationForm


class RegistrationView(BaseRegistrationView):
    form_class = RegistrationForm


class LoginView(BaseLoginView):
    authentication_form = AuthenticationForm
