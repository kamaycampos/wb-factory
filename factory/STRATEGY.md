# STRATEGY: this week's orders to the planner

Written by the **growth strategist** (daily cloud routine). The planner reads this BEFORE choosing
clips. It steers taste (what to pick, how to hook, when to post); it never overrides a gate, the
edges, compliance, `my_brand/lane.json` or `my_brand/BRAND.md`. Every order carries the number behind it.

**Score: $11.70 earned of $1,777,000** (all brands, 30 Sept; WB has earned $0 so far).

## 27 Oct 2026 (strategist; WB measured alone, never pooled with KT; 11 clips posted, 10 with 24h+ of data, ALL LOW)

### What the numbers say
- **Pace:** 7 posts in 7 days (20-26 Oct) = 1.0/day, on target. Yesterday 1 (20:33). **Queue is 4 deep:** 27 Oct 19:28, 28 Oct 20:06, 29 Oct 20:16, 30 Oct 20:17.
- **Instagram (7d, n=6, LOW):** median views **118**, median skip **53.5%**, shares+saves per 1k 1.9. The 7 days before (n=4): 155 views, skip 50.1, 11.4 per 1k. Views and shares fell on very few clips.
- **Best (14d, n=10):** "What 100 healthy 90-year-olds all ate" 199 views, skip 43.9 (148s, 16h); "Why your mom yelled at you" skip **34.9**, 132 views, YouTube 334 (99s, 20h); "What's stealing your sleep at night" skip 43.1, 122 views.
- **Worst (14d):** "What your cholesterol is really doing" 43 views, skip **79.4** (113s, 19h); "How to check your fish oil" skip 59.8; "What's leaching into your food" skip 59.3 (07h). "Why your vegan food isn't healthy": 6 Instagram views but 626 on YouTube, so Instagram probably did not distribute it.
- **Newest (under 24h, not scored):** "Why your cooking oil backfires" (26 Oct, 20h, 121s) 21 views, skip 68.4 on first read, YouTube 1. Early and LOW; "backfires" is an accusing verb.
- **Hook word (LOW):** Why n=3 median skip **40.0**; What n=2 skip 61.7 plus What's n=3 skip 55.5; The n=1 56.3; How n=1 59.8. Same direction as KT: What-openers lose.
- **Length (LOW):** over 120s n=1 skip 43.9; 76-120s n=2 57.2; 46-75s n=5 55.5; under 45s n=2 49.9. No usable pattern.
- **Hour (NY, LOW):** 20h n=4 median skip 47.2 (120 views); 19h n=3 skip 55.5 (43 views); 16h n=1 43.9; 22h n=1 56.3; 07h n=1 59.3.
- **CTA:** HEALTH offer n=9 skip 51.4, 119 views vs no CTA n=1 (178 views, skip 56.3): no split possible.
- **Others:** YouTube median 126 for the 7d window (n=6; mom 334, vegan 626 lead). DMs **0** since launch. TikTok: no data (tiktok.json empty). WB earned $0. No takedown seen in the manifest. Cinematic opener: not measurable (no `opener` field anywhere).

### Orders for the planner
1. **Never miss a day, keep 5+ clips stocked.** 4 are queued (to 30 Oct); add 2+ that pass `check_plan.py` and the render gates, 1 a day, best first. Do not fill a day with a weaker clip.
2. **Topics:** "what do I do" food, label and water clips first (90-year-olds, tap water, read the label, swap the oil, sleep). Information only, in Kevin's words ("Kevin Trudeau says...").
3. **Hooks:** `Why <everyday thing> ...` (n=3, skip 40.0), `What <number> healthy <people> ate`, `How to check/read your <thing>`. Avoid What-openers about organs or numbers (cholesterol: skip 79.4), a bare nutrient name as line one, accusing lines, and verbs like "lies", "leaching" or "backfires". Prefer Why/How over What for the queued clips.
4. **CTA:** every clip gets one; `HEALTH` offer on about 1 clip in 2, a question on the rest. Never none.
5. **Moments to skip:** vaccines, cancer, cures, stopping medication, harsh words anywhere in the clip, anything that reads as medical advice or an organ or blood-test claim. Two TikTok takedowns so far (both before 18 Oct); a third means review hooks before posting more.
6. **Length:** 90-150s story clips with a clear payoff first (148s: skip 43.9; 99s: 34.9); avoid 40-70s clips with no payoff. LOW.
7. **Posting hour:** keep 20:00 NY (n=4, skip 47.2); move the queued 19:28 slot (27 Oct, today) to 20:00 (19h skip 55.5, 43 views, n=3, LOW). Not 07:00. Change nothing else before n>=5 per hour.
8. **Openers:** the first 1080p-source clips get a calm cinematic opener (food, water, kitchen, golden light; never harsh or gloomy). Write `opener` into the series file so skip vs none can be read at n>=5 per side.

### Watch list
- **Queue depth:** 4 clips to 30 Oct; stock more by 29 Oct so 31 Oct is covered.
- Vegan clip: 6 Instagram views vs 626 on YouTube; check if Instagram restricted it.
- "Why your cooking oil backfires" (skip 68.4 at under 24h): re-read at 48h. First DM or first-comment keyword; first YouTube clip over 500 views.
- Any third takedown (2 so far, both TikTok).
- 29 Oct review: pace, takedowns, median skip under 45% on n>=10.
