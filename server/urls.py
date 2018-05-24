# -*- coding: utf-8 -*-
from server.index import IndexHandler

__author__ = 'neo'


# http server url
app_handlers = [
    # index page
    (r'/', IndexHandler),
]
