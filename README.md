# AiCoin API

Unofficial Python wrapper for [AiCoin](https://www.aicoin.com) public HTTP APIs — **stdlib only**, **no auth**, **no API key required**.

> Reverse-engineered from the AiCoin web app via Playwright XHR capture and JS bundle analysis.

## Usage

```python
from aicoin_api import *

# Global indices
indices = global_index()
for idx in indices:
    print(f"{idx['index_name']:<20} {idx['last']:<12} {idx['degree']}%")

# BTC technical signals
ss = side_summary('btcusdt:binance')
print(f"Signal rate: {ss['signal_rate']}  (0=bearish 1=bullish)")
print(f"Net inflow: {ss['main_net_inflow']} USD")
print(f"Long/Short ratio: {ss['btc_ls_ratio']}")

# Trading pair details
tp = tp_detail('btcusdt:binance')
o = tp[0]['open']['open']  # [ts, open, high, low, close, volume]

# News flash
news = hot_news()
print(news['latest_newsflash']['title'])

# Search
result = search_key('ETH')
print(result['data']['key'])
```

## API Reference

| Function | Returns | Description |
|----------|---------|-------------|
| `global_index()` | `List[Dict]` | 20+ real-time global indices (Nasdaq, Gold, BTC Fear & Greed, long/short ratios, crypto market cap) |
| `napi_indices()` | `List[Dict]` | On-chain indices (Gold, USD index, on-chain tokens) |
| `tp_detail(*symbols)` | `List[Dict]` | Trading pair details + 24h OHLCV |
| `side_summary(symbol)` | `Dict` | Technical signals · signal_rate / net inflow / BTC L/S ratio / liquidation |
| `fd_options(symbol)` | `List[Dict]` | Fund flow filter thresholds (BTC/ETH/Other × spot/futures/swap) |
| `market_chance(key)` | `Dict` | Market opportunities (signal win rate, arbitrage, gainers, breakouts) |
| `hot_news(coin_type)` | `Dict` | News flash + analyst long/short opinions |
| `custom_recommend(tp)` | `List[Dict]` | Recommended trading pairs or indices |
| `indicator_all_config()` | `Dict` | Full definitions for 78 technical indicators |
| `indicator_common()` | `Dict` | Lightweight indicator cache (19 main + 48 sub recommended) |
| `event_point(symbol)` | `List[List]` | Calendar event timestamps |
| `search_key(q)` | `Dict` | Search trading pairs |
| `geoip()` | `Dict` | IP geolocation |

### Dependencies

Zero — only Python stdlib (`urllib` + `json`).

### Symbol format

`{base}{quote}:{exchange}`, for example:

- `btcusdt:binance` — Binance BTC/USDT spot
- `btcswapusdt:okcoinfutures` — OKX BTC/USDT perpetual swap
- `solswapusdt:binance` — Binance SOL/USDT perpetual swap

Multiple symbols: `tp_detail('btcusdt:binance', 'ethusdt:binance')`.

### Field reference

#### `global_index()` item

| Field | Description |
|-------|-------------|
| `key` | Unique key `i:{name}:{source}` |
| `index_name` | Display name (Chinese) |
| `last` | Latest value |
| `degree` | Change % |
| `decimal` | Decimal places |

#### `side_summary()` fields

| Field | Description |
|-------|-------------|
| `signal_rate` | Technical signal rate (0~1, lower = more bearish) |
| `attend_score` | Attention/interest score |
| `main_net_inflow` | Net capital inflow (USD) |
| `btc_ls_ratio` | Long/Short position ratio |
| `btc_ls_signal` | Long/Short signal (1=bullish, -1=bearish) |
| `liq` | 24h liquidation volume |

#### `tp_detail()` structure

```json
{
  "key": "btcusdt:binance",
  "detail": { "en_name":"Bitcoin", "coin_show":"BTC",
              "market_en":"Binance", "trade_type":"spot", "instId":"BTCUSDT" },
  "open": { "open": [ts, open, high, low, close, volume] },
  "market": { "en_name":"Binance", "logo":"https://..." }
}
```

## Install

```bash
pip install aicoin-api
```

Or just copy `aicoin_api.py` into your project.

## License

MIT
