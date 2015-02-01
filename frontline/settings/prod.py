import os

from .base import *

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = False
TEMPLATE_DEBUG = False
