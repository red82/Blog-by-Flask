# -*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#whoosh
WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50


CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'


OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

# # mail server settings
# MAIL_SERVER = 'localhost'
# MAIL_PORT = 25
# MAIL_USERNAME = None
# MAIL_PASSWORD = None
#
# # administrator list
# ADMINS = ['andreyredkin82@gmail.com']

# email server
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'andreyredkin82@gmail.com'
MAIL_PASSWORD = 'starcraft2'

# administrator list
ADMINS = ['andreyredkin82@gmail.com']

# pagination
POSTS_PER_PAGE = 3

# available languages
LANGUAGES = {
    'en': 'English',
    'es': 'Español',
    'ru': 'Russian',
}
