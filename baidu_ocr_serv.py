# -*- coding: utf-8 -*-
import logging
import logging.handlers
import sys
import os
import tornado.httpserver
from tornado import ioloop
from server.urls import app_handlers
import ssl

__author__ = 'neo'


SERVER_PORT = 9999


def init_logging():
    """
    init logging module
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    sh = logging.StreamHandler()
    file_log = logging.handlers.TimedRotatingFileHandler('baidu_ocr_serv.log', 'MIDNIGHT', 1, 0)
    formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)-7s] [%(module)s:%(filename)s-%(funcName)s-%(lineno)d] %(message)s')
    sh.setFormatter(formatter)
    file_log.setFormatter(formatter)

    logger.addHandler(sh)
    logger.addHandler(file_log)

    logging.info("Current log level is : %s", logging.getLevelName(logger.getEffectiveLevel()))


def check_python_version():
    if sys.version[:1] != '3':
        return False
    else:
        return True


if __name__ == "__main__":
    try:
        if check_python_version() is False:
            print('Please use python3 run the program')
            exit()

        init_logging()

        # server configurations
        app = tornado.web.Application(
            handlers=app_handlers,
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )

        ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        ssl_ctx.load_cert_chain(os.path.join(os.path.join(os.path.dirname(__file__), "ca"), "server.crt"),
                                os.path.join(os.path.join(os.path.dirname(__file__), "ca"), "server.key"))

        api_server = tornado.httpserver.HTTPServer(app, xheaders=True, ssl_options=ssl_ctx)
        api_server.listen(SERVER_PORT)
        logging.info("Start server at: %d", SERVER_PORT)

        # start event loop
        ioloop.IOLoop.instance().start()
    except Exception as e:
        log_str = 'Server start fail! err = %s' % e
        logging.fatal(log_str)
