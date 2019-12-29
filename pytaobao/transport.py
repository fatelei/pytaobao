# -*- coding: utf8 -*-

import functools
import json
import logging
import datetime
import urllib3

from pytaobao import exceptions


class Transport(object):
    """Implement transport between api servers and clinet."""

    def __init__(self, endpoint):
        """Init.
        :param str endpoint: Api endpoint
        """
        self.endpoint = endpoint
        self.http_pool = urllib3.PoolManager()

    def perform_request(self, api: str, body: dict, method='GET'):
        """Perform request.
        :param str api: Api path
        :param dict body: Request body
        :param str method: HTTP method
        :return: HTTP response
        :raise: ConnectTimeoutError
        """
        body['method'] = api
        body['v'] = '2.0'
        body['timestamp'] = datetime.datetime.strftime('%Y-%m-%d+%H:%M:%S')
        func = functools.partial(self.http_pool.request, method, self.endpoint)
        if method == 'GET':
            resp = func(fields=body)
        else:
            resp = func(
                data=body,
                headers={'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
            )

        status, data = resp.status, resp.data
        if status >= 500:
            raise exceptions.TaobaoException(status, data)
        elif 400 <= status < 500:
            raise exceptions.ApiError(status, data)

        try:
            data = json.loads(data.decode('utf8'))
        except AttributeError:  # py3
            data = json.loads(data)

        if 'error_response' in data:
            errcode, errmsg = data['error_response'].pop('sub_code', 0), data.pop('sub_msg', '')
            logging.debug('Call api {} return ({}, {})'.format(api, errcode, errmsg))
            if errcode != 0:
                raise exceptions.ApiError(errcode, errmsg)
        return data
