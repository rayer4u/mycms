# -*- coding: utf-8 -*-
import logging
from registration.forms import RegistrationForm as BaseRegistrationForm
from django.contrib.auth.forms import AuthenticationForm as \
    BaseAuthenticationForm

logger = logging.getLogger(__name__)


class RegistrationForm(BaseRegistrationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        logger.debug(self.__repr__())
        logger.debug(self.__str__())

        # 把help_text放到placeholder里
        for field in self:
            field.field.widget.attrs['class'] = 'form-control'
            field.field.widget.attrs['aria-describedby'] = \
                'basic-'+field.id_for_label
            if (field.help_text):
                field.field.widget.attrs['placeholder'] = field.help_text


class AuthenticationForm(BaseAuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super(AuthenticationForm, self).__init__(request, *args, **kwargs)

        logger.info(self.__repr__())
        logger.info(dir(self))

        # 把help_text放到placeholder里
        for field in self:
            logger.info(type(field))
            logger.info(dir(field))

            field.field.widget.attrs['class'] = 'form-control'
            field.field.widget.attrs['aria-describedby'] = \
                'basic-'+field.id_for_label
            if (field.help_text):
                field.field.widget.attrs['placeholder'] = field.help_text
