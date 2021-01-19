#!/usr/bin/env python
# -*- coding: utf-8 -*- #


# Basic settings
AUTHOR = 'Rex Zhang'
SITENAME = 'RexZhang.com'
SITEURL = 'https://rexzhang.com'
DEFAULT_CATEGORY = '无类可归'

PATH = 'content'
DELETE_OUTPUT_DIRECTORY = True

STATIC_PATHS = [
    'images',

    'key',
]

# URL settings
RELATIVE_URLS = True
ARTICLE_URL = 'posts/{date:%Y}{date:%m}/{slug}'
ARTICLE_SAVE_AS = 'posts/{date:%Y}{date:%m}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Time and Date
TIMEZONE = 'Asia/Shanghai'
DEFAULT_DATE_FORMAT = '%Y/%m/%d'

DEFAULT_LANG = 'zh-Hans'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
    ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
    ('You can add links in your config file', '#'),
    ('Another social link', '#'),
)

# Pagination
DEFAULT_PAGINATION = True
PAGINATED_TEMPLATES = {
    'index': 10, 'tag': None, 'category': None, 'author': None
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Themes
SITESUBTITLE = '从记录到不仅仅是记录'
THEME = 'theme-rexzhang'
# THEME = 'themes/apricot'  # 字体非常漂亮
# THEME = 'themes/basic'
# THEME = 'themes/brutalist'
# THEME = 'themes/bootstrap'
# THEME = 'themes/clean-blog'
# THEME = 'themes/Flex'
# THEME = 'themes/gum'
# THEME = 'themes/hyde'
# THEME = 'themes/iris'
# THEME = 'themes/jesuislibre'  # 字体样式
# THEME = 'themes/nest'
# THEME = 'themes/nikhil-theme' # --
# THEME = 'themes/pujangga'  # error
# THEME = 'themes/SoMA2'
# THEME = 'themes/voce  # 漂亮 不能用
#
