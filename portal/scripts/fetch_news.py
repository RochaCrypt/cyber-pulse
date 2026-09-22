#!/usr/bin/env python3
"""
fetch_news.py — aggregate cybersecurity RSS feeds into news.json for the portal.
Author : Alexandre Rocha (github.com/RochaCrypt)

Publishes only headline, source, link and date (fair-use aggregation).
"""
import json
import time
from datetime import datetime, timezone

import feedparser

FEEDS = [
    ("The Hacker News", "https://feeds.feedburner.com/TheHackersNews"),
    ("BleepingComputer", "https://www.bleepingcomputer.com/feed/"),
    ("Krebs on Security", "https://krebsonsecurity.com/feed/"),
    ("Dark Reading", "https://www.darkreading.com/rss.xml"),
    ("SecurityWeek", "https://www.securityweek.com/feed/"),
    ("The Record", "https://therecord.media/feed/"),
    ("CISA Advisories", "https://www.cisa.gov/cybersecurity-advisories/all.xml"),
]
MAX_PER_FEED = 15
MAX_TOTAL = 80


def to_iso(entry):
    for key in ("published_parsed", "updated_parsed"):
        t = entry.get(key)
        if t:
            return datetime.fromtimestamp(time.mktime(t), tz=timezone.utc).isoformat()
    return None


def main():
    items = []
    for source, url in FEEDS:
        try:
            feed = feedparser.parse(url)
        except Exception as exc:  # noqa: BLE001
            print(f"[!] {source}: {exc}")
            continue
        for e in feed.entries[:MAX_PER_FEED]:
            title = (e.get("title") or "").strip()
            link = (e.get("link") or "").strip()
            if not title or not link:
                continue
            items.append({
                "title": title,
                "url": link,
                "source": source,
                "date": to_iso(e),
            })
        print(f"[+] {source}: {len(feed.entries[:MAX_PER_FEED])} items")

    # newest first; undated items sink to the bottom
    items.sort(key=lambda x: x["date"] or "", reverse=True)
    items = items[:MAX_TOTAL]

    out = {
        "updated": datetime.now(tz=timezone.utc).isoformat(),
        "count": len(items),
        "sources": [s for s, _ in FEEDS],
        "items": items,
    }
    with open("news.json", "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)
    print(f"[+] Wrote news.json ({len(items)} items)")


if __name__ == "__main__":
    main()
