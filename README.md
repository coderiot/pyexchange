*pyexchange* - Consistent API wrapper for cryptocurrency exchanges.

## Requirements

 - [requests](http://docs.python-requests.org/en/latest/)

## Installation
```sh
$ pip install -e git+https://github.com/coderiot/pyexchange.git#egg=pyexchange
```
## Supported exchanges
 - [Bitcurex](https://bitcurex.com/)
 - [Bitfinex](https://www.bitfinex.com/)
 - [Bitstamp](https://www.bitstamp.net/)
 - [BTCChina](https://btcchina.com/)
 - [BTC-e](https://btc-e.com/)
 - [CampBX](https://campbx.com/)
 - [Crypto-Trade](https://crypto-trade.com/)
 - [Cryptsy](https://crypto-trade.com/)
 - [Intersango](https://intersango.com/)
 - [Justcoin](https://justcoin.com/)
 - [localbitcions](https://localbitcoins.com/)
 - [mtgox](https://www.mtgox.com/)
 - [The Rock Trading](https://www.therocktrading.com/)

## Usage
### list supported exchanges
```python
>>> import pyexchange
>>> pyexchange.exchanges()
```

example Result:

```python
['bitcurex',
 'bitfinex',
 'bitstamp',
 'btcchina',
 'btce',
 'campbx',
 'cryptotrade',
 'cryptsy',
 'intersango',
 'justcoin',
 'localbitcoins',
 'mtgox',
 'rocktrading']
```

### create exchange by name with default market
```python
>>> import pyexchange
>>> ex = pyexchange.new_exchange('mtgox')
```

### create exchange by name and market
```python
>>> import pyexchange
>>> ex = pyexchange.new_exchange('mtgox', 'btc_eur')
```

### find available markets
```python
>>> import pyexchange
>>> pyexchange.find_market('btc_usd')
```

### list markets by exchange
```python
>>> import pyexchange
>>> ex = pyexchange.new_exchange('bitfinex')
>>> ex.markets()
```

or

```python
>>> pyexchange.exchange.bitfinex.markets()
```

Result:

```python
['ltc_btc', 'ltc_usd', 'btc_usd']
```

### set market for exchange
```python
>>> import pyexchange
>>> ex = pyexchange.new_exchange('mtgox')
>>> ex.market = 'btc_eur' # set market
>>> print ex.market # current market
```

### get exchange ticker
```python
>>> import pyexchange
>>> ex = pyexchange.new_exchange('mtgox')
>>> print ex.ticker()
```

Result:
```python
Ticker(avg=Decimal('157.19387'), high=Decimal('163.0'), low=Decimal('151.13324'), last=Decimal('160.0'), buy=Decimal('160.00001'), sell=Decimal('160.16'), vol=Decimal('22805.9081')
```

### get exchange orderbook
```python
>>> import pyexchange
>>> ex = pyexchange.new_exchange('mtgox')
>>> asks, bids = ex.depth()
>>> print asks
```

Result:
```python
[Order(price=Decimal('160.22457'), amount=Decimal('0.01')),
 Order(price=Decimal('160.22458'), amount=Decimal('0.12521962')),
 Order(price=Decimal('160.29347'), amount=Decimal('1')),
 Order(price=Decimal('160.36999'), amount=Decimal('2.56417803')),
 Order(price=Decimal('160.37'), amount=Decimal('7.98')),],
 ...
]
```

### get exchange trades
```python
>>> import pyexchange
>>> ex = pyexchange.new_exchange('mtgox')
>>> trades = ex.trades()
>>> print trades
```

Result:
```python
[Order(price=Decimal('160.22457'), amount=Decimal('0.01')),
 Order(price=Decimal('160.22458'), amount=Decimal('0.12521962')),
 Order(price=Decimal('160.29347'), amount=Decimal('1')),
 Order(price=Decimal('160.36999'), amount=Decimal('2.56417803')),
 Order(price=Decimal('160.37'), amount=Decimal('7.98')),
 ...
]
```
