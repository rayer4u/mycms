# -*- coding: utf-8 -*-
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import login as baseLogin
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from registration.backends.hmac.views import \
    RegistrationView as BaseRegistrationView

from .forms import AuthenticationForm, RegistrationForm


class RegistrationView(BaseRegistrationView):
    form_class = RegistrationForm


# @sensitive_post_parameters()
# @csrf_protect
# @never_cache
def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          current_app=None, extra_context=None):
    return baseLogin(request, template_name, redirect_field_name,
                     authentication_form, current_app, extra_context)
