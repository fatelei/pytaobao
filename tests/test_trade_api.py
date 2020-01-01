# -*- coding: utf8 -*-


from pytaobao.apis.trade import TradeApi


class TestTradeApi(object):

    @classmethod
    def setup_class(cls):
        cls.client = TradeApi(app_key='test',
                              app_secret='test',
                              session='test')
        cls.fields = 'tid,type,status,payment,orders,promotion_details'\
            ',buyer_open_uid,'\
            'receiver_phone,receiver_mobile,buyer_nick,' \
            'receiver_city,receiver_district,receiver_country,'\
            'receiver_name,post_fee,seller_rate,payment,pic_path,' \
            'consign_time,received_payment'

    def test_get_sold_trade(self):
        self.client.get_sold_trade(fields=self.fields)

    def test_get_trade_full_info(self):
        self.client.get_trade_full_info(fields=self.fields, tid=1)

    def test_get_trade_info(self):
        self.client.get_trade_info(fields=self.fields, tid=1)
