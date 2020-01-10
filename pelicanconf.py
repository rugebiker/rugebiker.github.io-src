#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = 'Ruben Guerra'
SITENAME = 'rugebiker'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = 'themes/MinimalXY'

## Theme customizations
#MINIMALXY_CUSTOM_CSS = 'static/custom.css'
#MINIMALXY_FAVICON = 'favicon.ico'
#MINIMALXY_START_YEAR = 2009
#MINIMALXY_CURRENT_YEAR = date.today().year

# Author
AUTHOR_INTRO = u'Hello world! I’m Rubén Guerra.'
AUTHOR_DESCRIPTION = u'Hello world! I’m Rubén Guerra. I like coffee, birds and Python.'
AUTHOR_AVATAR = 'http://www.gravatar.com/avatar/abcdefghijkl?s=240'
AUTHOR_WEB = 'http://www.rugebiker.com'

## Social
#SOCIAL = (
#    ('facebook', 'http://www.facebook.com/johndoe'),
#    ('twitter', 'http://twitter.com/johndoe'),
#    ('github', 'https://github.com/johndoe'),
#    ('linkedin', 'http://www.linkedin.com/in/johndoe'),
#)
#
## Menu
#MENUITEMS = (
#    ('Categories', '/' + CATEGORIES_SAVE_AS),
#    ('Archive', '/' + ARCHIVES_SAVE_AS),
#)

PAGE_ORDER_BY = 'page_order'
