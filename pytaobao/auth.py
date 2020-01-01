# -*- coding: utf8 -*-
"""
exmail.auth.
~~~~~~~~~~~~
Get access token by crop id and secret.
"""

import hashlib
import hmac


class Auth(object):
    """Get access token by crop id and secret."""

    def __init__(self, app_key: str, app_secret: str, sign_method: str):
        """Init.
        :param str app_key: App key
        :param str app_secret: App secret
        :param str sign_method:
        :param str endpoint:
        """
        self.app_key = app_key
        self.app_secret = app_secret
        self.sign_method = sign_method

    def generate_sign_code(self, params: dict) -> str:
        # https://open.taobao.com/doc.htm?spm=a219a.7386653.0.0.7663669aa6JW2E&source=search&docId=101617&docType=1
        keys = sorted(params.keys())
        if self.sign_method == 'md5':
            ary = [self.app_secret]
        for key in keys:
            value = params.get(key)
            if value:
                ary.append(str(key))
                ary.append(str(value))

        if self.sign_method == 'md5':
            ary.append(self.app_secret)

        sign_value = ''.join(ary).encode('utf8')
        if self.sign_method == 'md5':
            return hashlib.md5(sign_value).hexdigest().upper()
        elif self.sign_method == 'hmac':
            return hmac.new(self.app_secret, sign_value).hexdigest().upper()
