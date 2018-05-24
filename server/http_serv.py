import tornado.web
import logging

# -*- coding: utf-8 -*-
__author__ = 'neo'


class BaseHttpRequestHandler(tornado.web.RequestHandler):
    device_notify_list = []

    def __init__(self, application, request, **kwargs):
        super(BaseHttpRequestHandler, self).__init__(application, request, **kwargs)
        self._linkid = id(self)

    def data_received(self, chunk):
        pass

    def get_linkid(self):
        return self._linkid

    def on_finish(self):
        logging.info("This link[%d] finished" % self._linkid)
