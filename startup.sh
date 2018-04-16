#!/bin/sh
#pip install django-cms
#pip install aldryn-newsblog

. ../env/bin/activate
gunicorn -D -c gunicorn.py mycms.wsgi
