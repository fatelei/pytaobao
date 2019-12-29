# -*- coding: utf8 -*-

from pytaobao.auth import Auth
from pytaobao.transport import Transport


class TaobaoClient(object):

    def __init__(self, app_key: str, app_secret: str, endpoint: str):
        """Init.
        :param str app_key: App id
        :param str app_secret: App secret
        :param str endpoint: Api hostname
        """
        self._auth = Auth(app_key=app_key,
                          app_secret=app_secret)
        self._transport = Transport(endpoint=endpoint)

    @property
    def transport(self):
        return self._transport

    def generate_sign_code(self, params: dict):
        return self._auth.generate_sign_code
