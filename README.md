# aicoin-api

Unofficial Python wrapper for [AiCoin](https://www.aicoin.com) public APIs.
Stdlib only, no auth, no key.

## Install

```bash
pip install git+https://github.com/ArchdevilForge/aicoin-api.git
```

Or just copy `aicoin_api.py` into your project.

## Quick start

```python
from aicoin_api import *

# 20 global indices (Nasdaq, Gold, Fear & Greed...)
for idx in global_index():
    print(idx['index_name'], idx['last'], idx['degree']+'%')

# BTC technical signals
tp_detail('btcusdt:binance')   # 24h OHLCV
side_summary('btcusdt:binance') # signal_rate, net inflow, L/S ratio, liq

# News / search / geo
hot_news()
search_key('ETH')
geoip()
```

## API

| Function | Returns | |
|----------|---------|-|
| `global_index()` | 20 global indices | Nasdaq, Gold, Fear & Greed... |
| `tp_detail(*symbols)` | 24h OHLCV per pair | `btcusdt:binance` |
| `side_summary(symbol)` | signal_rate, net inflow, L/S ratio, liq | BTC technical signals |
| `napi_indices()` | on-chain indices | Gold, USD index, ... |
| `fd_options(symbol)` | fund flow filter thresholds | BTC/ETH × spot/futures |
| `market_chance(key)` | signal win rate, arbitrage, gainers | market opportunities |
| `hot_news(coin_type)` | news + analyst L/S opinions | |
| `custom_recommend(tp)` | 8 recommended pairs/indexes | |
| `indicator_all_config()` | 78 indicator definitions | |
| `indicator_common()` | 19 main + 48 sub indicator names | |
| `event_point(symbol)` | calendar timestamps | |
| `search_key(q)` | search trading pairs | |
| `geoip()` | IP geolocation | |

Symbol format: `{base}{quote}:{exchange}` — e.g. `btcusdt:binance`, `solswapusdt:okcoinfutures`.

## Example

See [`example.py`](example.py).

## License

MIT
