#!/usr/bin/env python3
"""AiCoin 公开 API — 纯 HTTP，无认证，无需 API Key。

用法:
  from aicoin_api import *
  data = global_index()
  for idx in data[:5]:
      print(idx['index_name'], idx['last'], idx['degree']+'%')
"""

from __future__ import annotations
import json
import urllib.request
import urllib.parse
from typing import Any, Dict, List, Optional

BASE_URL = "https://www.aicoin.com"

def fetch(path: str, params: Optional[Dict[str, str]] = None,
          body: Optional[Dict[str, Any]] = None,
          method: str = "GET") -> Dict[str, Any]:
    url = f"{BASE_URL}{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params, doseq=True)
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36", "Accept": "application/json"}
    if body is not None:
        data = json.dumps(body).encode()
        headers["Content-Type"] = "application/json"
    else:
        data = None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read())


def global_index() -> List[Dict[str, Any]]:
    """全球 20+ 个指数实时行情（纳斯达克、黄金、恐惧贪婪指数等）"""
    return fetch("/api/chart/quote/global-index").get("data", {}).get("list", [])

def market_chance(key: str = "") -> Dict[str, Any]:
    """市场机会：信号胜率、套利收益、涨幅榜、技术突破。key 为分页游标。"""
    return fetch("/api/chart/common/market-chance", params={"key": key} if key else None).get("data", {})

def hot_news(coin_type: Optional[str] = None, lang: str = "en") -> Dict[str, Any]:
    """快讯 + 分析师观点多空比。"""
    params: Dict[str, str] = {"lan": lang}
    if coin_type:
        params["coin_type"] = coin_type
    return fetch("/api/chart/kline/common/hot-news", params=params).get("data", {})

def tp_detail(*symbols: str) -> List[Dict[str, Any]]:
    """交易对详情 + 24h OHLCV。格式: btcusdt:binance"""
    if not symbols:
        return []
    return fetch("/api/chart/multi/tp-detail", params={"symbols": ",".join(symbols)}).get("data", {}).get("list", [])

def event_point(symbol: str = "btcusdt:binance") -> List[List[Any]]:
    """日历事件时间戳列表。"""
    return fetch("/api/chart/event/point", params={"symbol": symbol}).get("data", {}).get("list", [])

def napi_indices() -> List[Dict[str, Any]]:
    """链上指数（伦敦金、美元指数、on-chain 代币价格等）。"""
    return fetch("/napi/indices").get("data", [])

def indicator_all_config(lang: str = "en") -> Dict[str, Any]:
    """全部技术指标定义和参数配置。"""
    return fetch("/api/chart/indicator/all-config", params={"lan": lang}).get("data", {})

def fd_options(symbol: str = "btcusdt:binance") -> List[Dict[str, Any]]:
    """资金流向过滤器阈值。"""
    return fetch("/api/chart/config/fd-options", params={"symbol": symbol}).get("data", {}).get("filter", [])

def search_key(q: str) -> Dict[str, Any]:
    """搜索交易对。"""
    return fetch("/api/chart/market/search-key", body={"q": q}, method="POST")

def geoip() -> Dict[str, Any]:
    """IP 地理位置。"""
    return fetch("/api/common/geoip").get("data", {})

def custom_recommend(page: int = 1, page_size: int = 8,
                     tp: str = "tp", lang: str = "en") -> List[Dict[str, Any]]:
    """推荐交易对或指数。type='tp'=交易对 'index'=指数。"""
    return fetch("/api/common/custom/recommend",
                 params={"page": str(page), "page_size": str(page_size), "type": tp, "lan": lang}
                 ).get("data", {}).get("list", [])

def indicator_common(lang: str = "en") -> Dict[str, Any]:
    """轻量指标缓存。"""
    return fetch("/api/chart/indicator/common", params={"lan": lang}).get("data", {})

def side_summary(symbol: str = "btcusdt:binance",
                 open_time: int = 0, period: int = 60,
                 currency: str = "usd", lang: str = "en") -> Dict[str, Any]:
    """技术信号：signal_rate(多空), attend_score(关注度),
    main_net_inflow(主力净流入), btc_ls_ratio(多空比), liq(爆仓)。"""
    return fetch("/api/chart/stat/side-summary",
                 params={"symbol": symbol, "open_time": str(open_time),
                         "period": str(period), "currency": currency, "lan": lang}
                 ).get("data", {})
