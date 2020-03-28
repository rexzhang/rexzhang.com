#!/usr/bin/env python
# -*- coding: utf-8 -*- #


# Basic settings
AUTHOR = 'Rex Zhang'
SITENAME = 'RexZhang.com'
SITEURL = 'https://rexzhang.com'
DEFAULT_CATEGORY = '无类可归'

PATH = 'content'
DELETE_OUTPUT_DIRECTORY = True

# URL settings
RELATIVE_URLS = True
ARTICLE_URL = 'posts/{date:%Y}{date:%m}/{slug}'
ARTICLE_SAVE_AS = 'posts/{date:%Y}{date:%m}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Time and Date
TIMEZONE = 'Asia/Shanghai'
DEFAULT_DATE_FORMAT = '%Y/%m/%d'

DEFAULT_LANG = 'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
