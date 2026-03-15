#!/usr/bin/env python3
"""
Fetch market data for daily reports.
Usage:
  python3 fetch_market_data.py open   → morning data (premarket)
  python3 fetch_market_data.py close  → closing data
"""

import sys
import json
import csv
from datetime import datetime, date
import yfinance as yf

HOLDINGS_PATH = "portfolio/holdings.csv"

INDICES = {
    "SPY": "S&P 500",
    "QQQ": "Nasdaq 100",
    "DIA": "Dow Jones",
}

FUTURES = {
    "ES=F": "S&P 500 Futures",
    "NQ=F": "Nasdaq Futures",
    "YM=F": "Dow Futures",
}

SENTIMENT = {
    "^VIX": "VIX 恐慌指数",
    "GLD":  "黄金",
    "TLT":  "10Y 国债",
    "UUP":  "美元指数(ETF)",
}


def load_holdings():
    holdings = []
    with open(HOLDINGS_PATH, newline="") as f:
        for row in csv.DictReader(f):
            holdings.append({
                "ticker":       row["ticker"],
                "shares":       float(row["shares"]),
                "avg_cost":     float(row["avg_cost"]),
                "position_pct": float(row["position_pct"]),
            })
    return holdings


def fetch_quote(ticker):
    """Return latest price info for a single ticker."""
    # yfinance requires BRK-B format (dot → dash for class shares)
    yf_ticker = ticker.replace(".", "-")
    t = yf.Ticker(yf_ticker)
    info = t.fast_info
    try:
        current = info.last_price
        prev_close = info.previous_close
        if current is None or prev_close is None:
            hist = t.history(period="2d")
            if len(hist) >= 1:
                current = float(hist["Close"].iloc[-1])
                prev_close = float(hist["Close"].iloc[-2]) if len(hist) >= 2 else current
    except Exception:
        current, prev_close = None, None

    if current and prev_close:
        chg = current - prev_close
        chg_pct = chg / prev_close * 100
    else:
        chg = chg_pct = None

    return {
        "price":      round(current, 2) if current else None,
        "prev_close": round(prev_close, 2) if prev_close else None,
        "change":     round(chg, 2) if chg is not None else None,
        "change_pct": round(chg_pct, 2) if chg_pct is not None else None,
    }


def build_holdings_data(holdings):
    rows = []
    for h in holdings:
        q = fetch_quote(h["ticker"])
        price = q["price"]
        cost  = h["avg_cost"]
        total_return_pct = round((price - cost) / cost * 100, 2) if price else None
        market_value     = round(price * h["shares"], 0) if price else None
        unrealized_pnl   = round((price - cost) * h["shares"], 0) if price else None
        rows.append({
            **h,
            **q,
            "total_return_pct": total_return_pct,
            "market_value":     market_value,
            "unrealized_pnl":   unrealized_pnl,
        })
    return rows


def build_indices_data(symbols):
    result = {}
    for sym, name in symbols.items():
        q = fetch_quote(sym)
        result[sym] = {"name": name, **q}
    return result


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "close"
    holdings = load_holdings()

    data = {
        "mode":      mode,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "date":      date.today().isoformat(),
        "holdings":  build_holdings_data(holdings),
        "indices":   build_indices_data(INDICES),
        "sentiment": build_indices_data(SENTIMENT),
    }

    if mode == "open":
        data["futures"] = build_indices_data(FUTURES)

    print(json.dumps(data, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
