#! /usr/bin/python

# CherryBlogger - a minimal database free content management system 
#                 powering pietisticmonk.com/blog written in python
#                 using cherrypy, an efficient HTTP framework and 
#                 cherrytemplate a minimal templating engine in python.


__author__  = "Shiv Shankar Menon <shiv@pietisticmonk.com>"
__version__ = "0.1"


import cherrypy, os
from index import Index
from feeds import Feeds
from cache import Cache

if __name__ == "__main__":
    root = Index()
    root.feeds = Feeds()
    root.cache = Cache()
    cherrypy.config.update("blog.conf")
    cherrypy.quickstart(root, "/", "custom.conf")



