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

    def __init__(self, app_key: str, app_secret: str):
        """Init.
        :param str app_key: App key
        :param str app_secret: App secret
        """
        self.app_key = app_key
        self.app_secret = app_secret

    def generate_sign_code(self, params: dict, sign_type: str = 'md5') -> str:
        # https://open.taobao.com/doc.htm?spm=a219a.7386653.0.0.7663669aa6JW2E&source=search&docId=101617&docType=1
        keys = params.keys().sort()
        ary = [self.app_secret]
        for key in keys:
            value = params.get(key)
            if value:
                ary.append(str(key))
                ary.append(str(value))

        sign_value = ''.join(ary).encode('utf8')
        if sign_type == 'md5':
            return hashlib.md5(sign_value).hexdigest().upper(), sign_type
        elif sign_type == 'hmac':
            return hmac.new(sign_value).hexdigest().upper(), sign_type
