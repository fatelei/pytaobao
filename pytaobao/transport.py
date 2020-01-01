# -*- coding: utf8 -*-

import functools
import json
import logging
import datetime
import requests

from pytaobao import exceptions


class Transport(object):
    """Implement transport between api servers and clinet."""

    def __init__(self, endpoint):
        """Init.
        :param str endpoint: Api endpoint
        """
        self.endpoint = endpoint

    def perform_request(self, body: dict, method='GET'):
        """Perform request.
        :param str api: Api path
        :param dict body: Request body
        :param str method: HTTP method
        :return: HTTP response
        :raise: ConnectTimeoutError
        """
        if method == 'POST':
            resp = requests.post(self.endpoint, data=body)
        else:
            resp = requests.get(self.endpoint, data=body)

        status, data = resp.status_code, resp.text
        if status >= 500:
            raise exceptions.TaobaoException(status, data)
        elif 400 <= status < 500:
            raise exceptions.ApiError(status, data)
        data = json.loads(data)

        if 'error_response' in data:
            errcode, errmsg = data['error_response'].pop('sub_code', 0), data.pop('sub_msg', '')
            logging.debug('Call api {} return ({}, {})'.format(body, errcode, errmsg))
            if errcode != 0:
                raise exceptions.ApiError(errcode, errmsg)
        return data
