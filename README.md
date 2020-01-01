# pytaobao
taobao open [api](https://open.taobao.com/api.htm?docId=285&docType=2) in python

[![CircleCI](https://circleci.com/gh/fatelei/pytaobao.svg?style=svg)](https://circleci.com/gh/fatelei/pytaobao)

## Usage

### Using Specific Api Client

```
from pytaobao.apis.trade import TradeApi

fields = 'received_payment,receiver_country,receiver_town,pay_channel,title,pay_time'
cli = TradeApi(app_key='app_key',
               app_secret='app_secret',
               session='session')
tid = 'tid'
resp = taobao_cli.get_trade_fullinfo(fields=fields, tid=tid)
```

### Using Base Api Client

```
from pytaobao.apis.base import TaobaoClient

fields = 'received_payment,receiver_country,receiver_town,pay_channel,title,pay_time'
cli = TaobaoClient(app_key='app_key',
                   app_secret='app_secret',
                   session='session')
tid = 'tid'
params = {
    'fields': fields,
    'tid': tid
}
resp = taobao_cli.perform_request(api="taobao.trades.fullinfo.get",
                                  params=params)
```


- Required Parameter
  - app_key
  - app_secret
  - [session](https://open.taobao.com/doc.htm?docId=102635&docType=1&source=search)

- Optional Parameter
  - endpoint
    - default is `http://gw.api.taobao.com/router/rest`
    - for https is `https://eco.taobao.com/router/rest`
    

## Support Apis

- Trade Api
  - [taobao.trade.fullinfo.get](ttps://open.taobao.com/api.htm?docId=54&docType=2)
  - [taobao.trade.get](https://open.taobao.com/api.htm?docId=47&docType=2)
  - [taobao.trades.sold.get](https://open.taobao.com/api.htm?docId=46&docType=2)

- Trade Rate Api
  - [taobao.traderates.get](https://open.taobao.com/api.htm?docId=55&docType=2)
  - [tmall.traderate.feeds.get](https://open.taobao.com/api.htm?docId=22532&docType=2)
