# -*- coding: utf8 -*-

import datetime

from pytaobao.auth import Auth
from pytaobao.transport import Transport


class TaobaoClient(object):

    def __init__(self, app_key: str, app_secret: str, endpoint: str, session: str, sign_method: str = 'md5'):
        """Init.
        :param str app_key: App id
        :param str app_secret: App secret
        :param str endpoint: Api hostname
        :param str session:
        :param str sign_method:
        """
        self._auth = Auth(app_key=app_key,
                          app_secret=app_secret,
                          sign_method=sign_method,
                          session=session)
        self._transport = Transport(endpoint=endpoint)

    @property
    def transport(self):
        return self._transport

    def wrap_common_field(self, params: dict) -> dict:
        params['sign_method'] = self._auth.sign_method
        params['session'] = self._auth.session
        params['app_key'] = self._auth.app_key
        params['v'] = '2.0'
        params['format'] = 'json'
        params['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return params

    def generate_sign_code(self, params: dict):
        return self._auth.generate_sign_code(params=params)
