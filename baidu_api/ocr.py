# -*- coding: utf-8 -*-
from aip import AipOcr
import logging

__author__ = 'neo'

APP_ID = '10699041'
API_KEY = 'kPHBQBbptX6t8fjK2EAkGU90'
SECRET_KEY = 'Xukj70GVa1qqLxGc5LkniT1CQ7FszumS '


def init_api(connection_timeout=None, socket_timeout=None):
    try:
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

        if connection_timeout is not None:
            client.setConnectionTimeoutInMillis(connection_timeout)

        if socket_timeout is not None:
            client.setSocketTimeoutInMillis(socket_timeout)

        return client
    except Exception as err:
        logging.error("AipOcr Client fail! err = {}".format(err))
        return None


def pic_basic_general(api_client, image, options=None):
    if image is None or api_client is None:
        return 0, []

    if options is None:
        options = {}

    try:
        options["detect_direction"] = "true"
        options["detect_language"] = "true"
        options["probability"] = "true"

        res = api_client.basicGeneral(image, options)
        return res['words_result_num'], res['words_result']
    except Exception as err:
        logging.error("pic_basic_general fail! err = {}".format(err))
        return 0, []


def pic_basic_accurate(api_client, image, options=None):
    if image is None or api_client is None:
        return 0, []

    if options is None:
        options = {}

    try:
        options['detect_direction'] = "true"
        options['probability'] = 'true'

        res = api_client.basicAccurate(image, options)
        return res['words_result_num'], res['words_result']
    except Exception as err:
        logging.error("pic_basic_accurate fail! err = {}".format(err))
        return 0, []