#!/usr/bin/env python3
"""EVERY DAY HAS CLIPS FOR TIKTOK (15 Nov 2026).

Kamay: "WB is not getting clips to post." After the two strikes the hold list was widened
(state/tiktok_avoid.json) and a held clip still posts on Instagram, Facebook and YouTube - but
nothing looked at WHICH DAY the TikTok-safe clips fell on. Since the widening 1 of 3 clips
reached his inbox, and the next two slots were both held: a whole day with almost nothing to post.

This only SWAPS the hours of clips that are still waiting: a day short of TikTok-safe clips
takes one from a later day that has more than it needs, and gives a held clip back in exchange.
Nothing is added, dropped or posted twice; the other platforms get the same number of clips a
day as before. Runs before every posting pass; prints what it moved.

    python factory/tiktok_balance.py [--dry]
"""
import json
import os
import sys
from datetime import datetime, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path = [p for p in sys.path if os.path.abspath(p or ".") != HERE]      # factory/queue.py must not hide Python's own queue
sys.path.insert(0, os.path.join(ROOT, "engine"))
MAN = os.path.join(ROOT, "state", "manifest.json")
WANT = int(os.environ.get("TIKTOK_PER_DAY", "3"))       # TikTok-safe clips wanted each day
DAYS = 7


def main(dry=False):
    import poster
    try:
        from zoneinfo import ZoneInfo
        now = datetime.now(ZoneInfo(os.environ.get("KT_TZ", "America/New_York"))).replace(tzinfo=None)
    except Exception:
        now = datetime.utcnow()
    man = json.load(open(MAN))
    edge = (now + timedelta(minutes=40)).strftime("%Y-%m-%dT%H:%M")       # never touch a slot about to fire
    wait = [c for c in man["clips"] if not c.get("done") and not c.get("posted_at") and not c.get("posting")
            and (c.get("scheduled_at") or "") > edge and not c.get("solo")]
    safe = lambda c: not poster.tiktok_risk(c)
    day = lambda c: c["scheduled_at"][:10]
    days = sorted({day(c) for c in wait})[:DAYS]
    moved = 0
    for d in days:
        while True:
            here = [c for c in wait if day(c) == d]
            have = sum(1 for c in here if safe(c))
            held = [c for c in here if not safe(c)]
            if have >= min(WANT, len(here)) or not held:
                break
            # a later day that keeps at least WANT after giving one (the furthest such day first)
            donor = None
            for d2 in sorted({day(c) for c in wait if day(c) > d}, reverse=True):
                there = [c for c in wait if day(c) == d2 and safe(c)]
                if len(there) > (WANT if d2 in days else 0):
                    donor = there[-1]
                    break
            if donor is None:
                for d2 in sorted({day(c) for c in wait if day(c) > d}, reverse=True):   # nobody has spare: share
                    there = [c for c in wait if day(c) == d2 and safe(c)]
                    if len(there) > have + 1:
                        donor = there[-1]
                        break
            if donor is None:
                break
            h = held[0]
            h["scheduled_at"], donor["scheduled_at"] = donor["scheduled_at"], h["scheduled_at"]
            for c in (h, donor):
                c.pop("stale", None)
            moved += 1
            print(f"  {d}: {donor['file'].split('/')[-1][:44]} comes forward for TikTok; "
                  f"{h['file'].split('/')[-1][:40]} takes its hour on {h['scheduled_at'][:10]}")
    wait2 = [c for c in man["clips"] if not c.get("done") and not c.get("posted_at") and (c.get("scheduled_at") or "") > edge]
    print("tiktok balance:", ", ".join(f"{d[5:]} {sum(1 for c in wait2 if day(c) == d and safe(c))}/{sum(1 for c in wait2 if day(c) == d)}"
                                       for d in sorted({day(c) for c in wait2})[:DAYS]), f"({moved} swap(s))")
    if moved and not dry:
        json.dump(man, open(MAN, "w"), indent=1)
    return moved


if __name__ == "__main__":
    main("--dry" in sys.argv)
