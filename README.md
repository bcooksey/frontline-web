# Frontline Web

This project is the web frontend for the [Frontline](https://github.com/bcooksey/Frontline) project.

# Requirements

1. Python 3.4+
1. (Recommended) virtualenv and virtualenv wrapper. These get installed on your system globally, then you do the install process below inside a virtualenv

# Install

1. Install dependencies `pip install -r requirements/dev.txt`
1. Setup a barebones settings file (tweak it as you like) `echo "from .dev import *" >> frontline/settings/local.py`
1. Setup database `./manage.py migrate`
1. Add yourself as a superuser `./manage.py createsuperuser`
1. Start the server! `./manage.py runserver`
