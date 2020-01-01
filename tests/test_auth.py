# -*- coding: utf8 -*-

from pytaobao.auth import Auth


class TestAuth(object):

    def test_generate_sign_code(self):
        auth = Auth(app_key='a', app_secret='b', sign_method='md5')
        auth.generate_sign_code(params={'a': 1})
