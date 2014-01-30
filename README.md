*pyexchange* - Consistent API wrapper for cryptocurrency exchanges.

## Requirements

 - [requests](http://docs.python-requests.org/en/latest/)

## Installation
```sh
$ pip install -e git+https://github.com/coderiot/pyexchange.git#egg=pyexchange
```
## Supported exchanges
| Exchange Name | Public Api    | Private Api   |
| ------------- | ------------- | ------------- |
| [Bitcurex](https://bitcurex.com/)                    | Yes  | No  |
| [Bitfinex](https://www.bitfinex.com/)                | Yes  | No  |
| [Bitstamp](https://www.bitstamp.net/)                | Yes  | No  |
| [BTCChina](https://btcchina.com/)                    | Yes  | No  |
| [BTC-e](https://btc-e.com/)                          | Yes  | No  |
| [CampBX](https://campbx.com/)                        | Yes  | No  |
| [Crypto-Trade](https://crypto-trade.com/)            | Yes  | Yes (not tested)|
| [Cryptsy](https://crypto-trade.com/)                 | Yes  | Yes (not tested)  |
| [Intersango](https://intersango.com/)                | Yes  | No  |
| [Justcoin](https://justcoin.com/)                    | Yes  | No  |
| [localbitcions](https://localbitcoins.com/)          | Yes  | No  |
| [mtgox](https://www.mtgox.com/)                      | Yes  | No  |
| [The Rock Trading](https://www.therocktrading.com/)  | Yes  | No  |
| [Bter](https://www.bter.com/)                        | Yes  | Yes (without tests)  |
| [Coins-e](https://www.coins-e.com/)                  | Yes  | Yes (not tested)|
| [Vircurex](https://www.vircurex.com/)                | Yes  | No  |
| [CoinEx](https://www.coinex.pw/)                     | Yes  | No  |

## runnning tests
```python
python -m pyexchange.tests -v
```

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
