# -*- coding: utf8 -*-

from pytaobao.apis.base import TaobaoClient
from pytaobao.helper import required_params


class RateApi(TaobaoClient):

    @required_params('fields', 'rate_type', 'role')
    def get_taobao_trade_rates(self,
                               fields,
                               rate_type: str,
                               role: str,
                               result: str = None,
                               tid: str = None,
                               num_iid: int = None,
                               start_date: str = None,
                               end_date: str = None,
                               page_no: int = 1,
                               page_size: int = 40,
                               use_has_next: bool = True):
        """https://open.taobao.com/api.htm?docId=55&docType=2

        :param fields:
        :param rate_type:
        :param role:
        :param result:
        :param tid:
        :param num_iid:
        :param start_date:
        :param end_date:
        :param page_no:
        :param page_size:
        :param use_has_next:
        :return:
        """

        params = {
          'page_no': page_no,
          'page_size': page_size,
          'role': role,
          'rate_type': rate_type,
          'fields': fields
        }
        if start_date:
            params['start_date'] = start_date

        if end_date:
            params['end_date'] = end_date

        if result:
            params['result'] = result

        if num_iid:
            params['num_iid'] = num_iid

        if tid:
            params['tid'] = tid

        return self.perform_request(api='taobao.traderates.get',
                                    params=params)

    @required_params('child_trade_id')
    def get_tmall_child_trade_traderate(self, child_trade_id: int):
        """https://open.taobao.com/api.htm?docId=22532&docType=2

        :param child_trade_id:
        :return:
        """
        params = {
          'child_trade_id': child_trade_id,
          'method': 'tmall.traderate.feeds.get'
        }

        return self.perform_request(api='tmall.traderate.feeds.get',
                                    params=params)

    @required_params('fields', 'tid')
    def get_trade_info(self, fields: str, tid: int):
        """https://open.taobao.com/api.htm?docId=47&docType=2

        :param fields:
        :param tid:
        :return:
        """
        params = {
          'fields': fields,
          'tid': tid,
          'method': 'taobao.trade.get'
        }
        params = self.wrap_common_field(params)
        return self._transport.perform_request('taobao.trade.get', params, 'POST')
