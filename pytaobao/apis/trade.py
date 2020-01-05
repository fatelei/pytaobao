# -*- coding: utf8 -*-

from pytaobao.apis.base import TaobaoClient
from pytaobao.helper import required_params


class TradeApi(TaobaoClient):

    @required_params('fields')
    def get_sold_trade(self,
                       fields,
                       start_created: str = None,
                       end_created: str = None,
                       status: str = None,
                       buyer_nick: str = None,
                       _type: str = None,
                       ext_type: str = None,
                       rate_status: str = None,
                       tag: str = None,
                       page_no: int = 1,
                       page_size: int = 40,
                       use_has_next: bool = True,
                       buyer_open_id: str = None):
        """https://open.taobao.com/api.htm?docId=46&docType=2

        :param fields:
        :param start_created:
        :param end_created:
        :param status:
        :param buyer_nick:
        :param _type:
        :param ext_type:
        :param rate_status:
        :param tag:
        :param page_no:
        :param page_size:
        :param use_has_next:
        :param buyer_open_id:
        :return:
        """
        params = {
          'page_no': page_no,
          'page_size': page_size,
          'fields': fields
        }
        if start_created:
            params['start_created'] = start_created

        if end_created:
            params['end_created'] = end_created

        if status:
            params['status'] = status

        if buyer_nick:
            params['buyer_nick'] = buyer_nick

        if _type:
            params['type'] = _type

        if ext_type:
            params['ext_type'] = ext_type

        if rate_status:
            params['rate_status'] = rate_status

        if tag:
            params['tag'] = tag

        params['use_has_next'] = 'true' if use_has_next else 'false'
        if buyer_open_id:
            params['buyer_open_id'] = buyer_open_id

        return self.perform_request(api='taobao.trades.sold.get',
                                    params=params)

    @required_params('fields', 'tid')
    def get_trade_full_info(self, fields: str, tid: int):
        """https://open.taobao.com/api.htm?docId=54&docType=2

        :param fields:
        :param tid:
        :return:
        """
        params = {
          'fields': fields,
          'tid': tid
        }
        return self.perform_request(api='taobao.trade.fullinfo.get',
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
          'tid': tid
        }
        return self.perform_request(api='taobao.trade.get',
                                    params=params)
