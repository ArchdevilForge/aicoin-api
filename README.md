# AiCoin API

AiCoin 网站的公开 HTTP API 封装，**纯标准库**，**无认证**，**无需 API Key**。

> 逆向工程自 [aicoin.com](https://www.aicoin.com)，通过 Playwright 捕获 XHR/JS bundle 发现接口路径。

## 用法

```python
from aicoin_api import *

# 全球指数行情
indices = global_index()
for idx in indices:
    print(f"{idx['index_name']:<20} {idx['last']:<12} {idx['degree']}%")

# BTC/USD 技术多空信号
ss = side_summary('btcusdt:binance')
print(f"信号率: {ss['signal_rate']}  (0=看空 1=看多)")
print(f"主力净流入: {ss['main_net_inflow']} USD")
print(f"多空比: {ss['btc_ls_ratio']}  (1=看多 -1=看空)")

# 交易对详情
tp = tp_detail('btcusdt:binance')
o = tp[0]['open']['open']  # [ts, open, high, low, close, volume]

# 资讯快讯
news = hot_news()
print(news['latest_newsflash']['title'])

# 搜索交易对
result = search_key('ETH')
print(result['data']['key'])
```

## 接口列表

| 函数 | 返回 | 说明 |
|------|------|------|
| `global_index()` | `List[Dict]` | 20+ 全球指数实时行情（纳指/黄金/BTC恐惧贪婪/多空持仓比/加密总市值等） |
| `napi_indices()` | `List[Dict]` | 链上指数（伦敦金/美元指数/on-chain 代币） |
| `tp_detail(*symbols)` | `List[Dict]` | 交易对详情 + 24h OHLCV |
| `side_summary(symbol)` | `Dict` | 技术多空信号 · signal_rate / 主力净流入 / BTC多空比 / 爆仓 |
| `fd_options(symbol)` | `List[Dict]` | 资金流向过滤器阈值（BTC/ETH/其他 × 现货/合约/永续） |
| `market_chance(key)` | `Dict` | 市场机会（信号胜率/套利收益/涨幅榜/技术突破） |
| `hot_news(coin_type)` | `Dict` | 快讯 + 分析师多空观点 |
| `custom_recommend(tp)` | `List[Dict]` | 推荐交易对或指数 |
| `indicator_all_config()` | `Dict` | 78 种技术指标完整定义参数 |
| `indicator_common()` | `Dict` | 轻量指标缓存（19 主图 + 48 副图推荐） |
| `event_point(symbol)` | `List[List]` | 日历事件时间戳 |
| `search_key(q)` | `Dict` | 搜索交易对 |
| `geoip()` | `Dict` | IP 地理位置 |

### 依赖

零依赖，仅用 Python 标准库 `urllib` + `json`。

### 符号格式

交易对符号格式为 `{base}{quote}:{exchange}`，例如：

- `btcusdt:binance` — 币安 BTC/USDT 现货
- `btcswapusdt:okcoinfutures` — OKX BTC/USDT 永续
- `solswapusdt:binance` — 币安 SOL/USDT 永续

支持同时查询多个：`tp_detail('btcusdt:binance', 'ethusdt:binance')`。

### 数据示例

#### `global_index()` 返回字段

| 字段 | 说明 |
|------|------|
| `key` | 唯一键 `i:{name}:{source}` |
| `index_name` | 中文名称 |
| `last` | 最新值 |
| `degree` | 涨跌幅 % |
| `decimal` | 小数位 |

#### `side_summary()` 返回字段

| 字段 | 说明 |
|------|------|
| `signal_rate` | 技术信号率 (0~1, 越低越看空) |
| `attend_score` | 关注度 |
| `main_net_inflow` | 主力净流入 (USD) |
| `btc_ls_ratio` | 多空持仓比 |
| `btc_ls_signal` | 多空信号 (1=看多, -1=看空) |
| `liq` | 24h 爆仓量 |

#### `tp_detail()` 结构

```json
{
  "key": "btcusdt:binance",
  "detail": { "cn_name":"比特币", "en_name":"Bitcoin", "coin_show":"BTC",
              "market_cn":"币安", "trade_type":"spot", "instId":"BTCUSDT" },
  "open": { "open": [ts, open, high, low, close, volume] },
  "market": { "cn_name":"币安", "logo":"https://..." }
}
```

## 安装

```bash
pip install aicoin-api
```

或者直接复制 `aicoin_api.py` 到项目中使用。

## 许可

MIT
