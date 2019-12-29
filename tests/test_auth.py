# -*- coding: utf8 -*-
"""
tests.test_auth.
~~~~~~~~~~~~~~~~~~~
Unittest for `exmail.auth.Auth`.
"""

import pytest

from pytaobao.auth import Auth


class TestAuth(object):

    @pytest.fixture(autouse=True)
    def test_generate_sign_code(self):
        auth = Auth(app_key='a', app_secret='b')
        auth.generate_sign_code(params={'a': 1})
