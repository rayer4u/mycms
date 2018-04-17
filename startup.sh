#!/bin/sh
#pip install django-cms
#pip install aldryn-newsblog

. ../env/bin/activate

export DJANGO_SETTINGS_MODULE=mycms.settings.prod
gunicorn -D -c gunicorn.py mycms.wsgi
