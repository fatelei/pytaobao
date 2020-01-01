# -*- coding: utf8 -*-

import pytest
import requests


class MockResponse(object):

    @property
    def status_code(self):
        return 200

    @staticmethod
    def json():
        return {"mock_key": "mock_response"}

    @property
    def text(self):
        return '{"mock_key": "mock_response"}'


@pytest.fixture(autouse=True)
def mock_response(monkeypatch):
    """Requests.get() mocked to return {'mock_key':'mock_response'}."""

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "post", mock_get)
