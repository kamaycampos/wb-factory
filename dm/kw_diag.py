"""READ-ONLY (15 Nov 2026): how did people SPELL the comment word, and did the account answer?
Meta's own comment rule treats each spelling as its own keyword (found on KT the same day:
"Wish" typed on a phone was not "WISH" or "wish"). Prints the exact text of every comment that
holds one of the words, in any case, and whether the account replied under it. No names."""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import dm_reply as m
WORDS = [w.strip().lower() for w in (os.environ.get("KW_WORDS") or "health,ebook").split(",")]
ig, tok = m.env("IG_USER_ID"), (m.env("FB_ACCESS_TOKEN") or m.env("IG_ACCESS_TOKEN"))
mine = m._get(f"{m.G}/{ig}", {"fields": "username", "access_token": tok}).get("username", "")
media, url, params = [], f"{m.G}/{ig}/media", {"fields": "id,timestamp,comments_count", "limit": 100, "access_token": tok}
while url and len(media) < 150:
    j = m._get(url, params); media += j.get("data", []); url, params = (j.get("paging") or {}).get("next"), {}
n = hidden = 0
for p in media:
    if not p.get("comments_count"):
        continue
    cs = m._get(f"{m.G}/{p['id']}/comments", {"fields": "id,text,timestamp,username,replies{username}", "limit": 50, "access_token": tok}).get("data", [])
    got = len(cs) + sum(len((c.get("replies") or {}).get("data", [])) for c in cs)
    hidden += max(0, p["comments_count"] - got)
    for c in cs:
        t = c.get("text") or ""
        if c.get("username") == mine or not any(w in t.lower() for w in WORDS):
            continue
        n += 1
        answered = any(r.get("username") == mine for r in (c.get("replies") or {}).get("data", []))
        print(f"{c['timestamp'][:16]} text={t[:30]!r} answered_by_the_account={answered}")
print(f"posts read {len(media)}, keyword comments {n}, comments Instagram counted but did not hand over {hidden}")
