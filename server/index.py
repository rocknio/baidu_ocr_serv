# -*- coding: utf-8 -*-
from server.http_serv import BaseHttpRequestHandler
from baidu_api.ocr import init_api, pic_basic_accurate
import logging

__author__ = 'neo'


class IndexHandler(BaseHttpRequestHandler):
    def get(self):
        try:
            self.render("index.html", words_result=None)
        except Exception as err:
            self.set_status(500)
            self.write("Internal error!")
            logging.exception("IndexHandler error!, err = {}".format(err))

    def post(self):
        try:
            # upload_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)), 'pics')
            file_metas = self.request.files.get('file', None)

            if not file_metas:
                logging.error("Can't get upload file metas, redirect to index page...")
                self.redirect("/")
            else:
                for meta in file_metas:
                    # filename = meta['filename']
                    # file_path = os.path.join(upload_path, filename)
                    #
                    # with open(file_path, "wb") as upload_file:
                    #     upload_file.write(meta['body'])

                    logging.info("start ocr...{}".format(meta['filename']))
                    baidu_client = init_api()
                    text_count, text = pic_basic_accurate(baidu_client, meta['body'])
                    logging.info("end ocr...{}".format(meta['filename']))
                    words_result = None
                    if text_count > 0:
                        words_result = []
                        for words in text:
                            words_result.append(words["words"])

                    self.render("index.html", words_result=words_result)
        except Exception as err:
            self.set_status(500)
            self.write("Internal error!")
            logging.exception("IndexHandler error!, err = {}".format(err))
