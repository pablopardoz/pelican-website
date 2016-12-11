#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'pablo pardo'
SITENAME = u'pablo pardo zaragoza'
SITEURL = ''
FRONTP= 'pages/home.html'
INDEX_SAVE_AS = 'blog_index.html'
PATH = 'content'
#THEME = '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/pelican/themes/flasky'
THEME = '/Users/pablo/blog/themes/flasky'
TIMEZONE = 'Europe/Paris'
STATIC_PATHS = ['images', 'pdfs']

DEFAULT_LANG = u'es'

DEFAULT_CATEGORY = 'Uncategorized'
DATE_FORMAT = {
'en': '%d %m %Y'
}
DEFAULT_DATE_FORMAT = '%d %m %Y'
DEFAULT_PAGINATION = 10
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'


#PROFILE_IMAGE="http://4.bp.blogspot.com/-sjhx8zCwp4w/UW1mV6t1v2I/AAAAAAAAAJw/ZFzWlW4fupc/s1600/cabecera.jpg"



# Navigation sections and relative URL:
SECTIONS = [
	('about', 'pages/about.html'),
	('projects', 'pages/projects.html'),
	('blog', 'blog_index.html')
	]

#LICENSE_NAME = 'yo mismo'
PAGE_PATHS = ['pages']
PAGES_ON_MENU=False
MAIL_USERNAME = 'pardozaragoza'
MAIL_HOST = 'gmail.com'
TWITTER_USERNAME="ppardozz"
GITHUB_URL = 'http://github.com/pablopardoz'
LINKEDIN_URL='https://es.linkedin.com/in/pablo-pardo-97147534'
SO_ADDRESS = "#"
SHOW_ARTICLE_AUTHOR=False
DISPLAY_PAGES_ON_MENU = False
# # Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('You can modify those links in your config file', '#'),)

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

# DEFAULT_PAGINATION = 10

# # Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#pelican /path/to/your/content/ [-s path/to/your/settings.py]
#pelican /Users/pablo/blog/output -s /Users/pablo/blog/output
#s3cmd sync output/ --acl-public --guess-mime-type s3://pablopardoes
