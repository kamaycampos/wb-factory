# STRATEGY: this week's orders to the planner

Written by the **growth strategist** (daily cloud routine). The planner reads this BEFORE choosing
clips. It steers taste (what to pick, how to hook, when to post); it never overrides a gate, the
edges, compliance, `my_brand/lane.json` or `my_brand/BRAND.md`. Every order carries the number behind it.

**Score: $11.70 earned of $1,777,000** (all brands, 30 Sept; WB has earned $0 so far).

## 24 Oct 2026 (strategist; WB measured alone, never pooled with KT; 8 clips posted since 15 Oct, 7 with 24h+ of data, ALL LOW)

### What the numbers say
- **Pace:** 6 posts in 7 days (17-23 Oct; none on 18 Oct) = 0.86/day vs 1/day. Yesterday (23 Oct) 1 (fish oil, 20:11). Today 1 queued (24 Oct 20:17); **nothing is scheduled after that.**
- **Instagram (7d, n=6, LOW):** median views **109**, median skip **57.5%**, shares+saves per 1k 12.6. The 7 days before are n=2 (median 165 views, skip 39.1), so views fell and skip rose, but on 2 clips.
- **Best (14d, n=7):** "What 100 healthy 90-year-olds all ate" 199 views, skip 43.9, 148s (16h); "The real vitamin E you're missing" 177, skip 56.0 (60s, 22h, no CTA); "Why your mom yelled at you" skip **34.3**, 131 views, 99s (20h), YouTube 328 (TikTok removed it).
- **Worst (14d):** "What your cholesterol is really doing" 42 views, skip **81.8**, 113s (19h); "What's leaching into your food" 103 views, skip 58.9 (68s, 07h); "Why your vegan food isn't healthy" 3 views on Instagram (42s, 19h) but 424 on YouTube, so Instagram likely did not distribute it.
- **Hook word (LOW):** Why n=3 median skip 50.0; What n=2 skip 62.8 (+ What's n=1 58.9); The n=1 56.0. Same direction as KT: What-openers lose.
- **Length (LOW):** over 120s n=1 skip 43.9; 76-120s n=2 skip 58.0; 46-75s n=3 skip 56.0. No usable pattern.
- **Hour (NY, LOW):** 20h n=2 median skip 42.6 (124 views); 16h n=1 43.9; 19h n=2 skip 65.9 (22 views); 22h n=1 56.0; 07h n=1 58.9.
- **CTA:** offer (HEALTH) n=6 skip 50.5, 110 views vs no CTA n=1 (177 views, skip 56.0): no split possible.
- **Others:** YouTube median 13.5 views (n=6); only mom (328) and vegan (424) are higher. DMs **0** since launch. TikTok: no data (tiktok.json empty). Score WB $0.
- **Cinematic opener:** not measurable (no `opener` field in kt_series.json or metrics; release not readable here).

### Orders for the planner
1. **Never miss a day.** Only one clip is queued (24 Oct). Stock and schedule 5+ clips that pass `check_plan.py` and the render gates, 1 a day, best first; do not fill a day with a weaker clip.
2. **Topics:** "what do I do" food, label and water clips first (90-year-olds, read the label, tap water, swap the oil, check your fish oil). Information only, in Kevin's words ("Kevin Trudeau says...").
3. **Hooks:** `Why <everyday thing> ...`, `What <number> healthy <people> ate`, `How to check/read your <thing>`. Avoid What-openers about organs or numbers (cholesterol: skip 81.8), a bare nutrient name as line one, accusing lines, and verbs like "lies" or "leaching".
4. **CTA:** every clip gets one; `HEALTH` offer on about 1 clip in 2, a question on the rest. Never none (the no-CTA clip also lost on skip).
5. **Moments to skip:** vaccines, cancer, cures, stopping medication, harsh words anywhere in the clip, anything that reads as medical advice or a reading/blood-test claim. Two TikTok takedowns so far; a third means review hooks before posting more.
6. **Length:** 90-150s story clips with a clear payoff first (148s: best skip 43.9; 99s: 34.3); avoid 45-70s clips with no payoff. LOW.
7. **Posting hour:** keep 20:00 NY (n=2, skip 42.6); not 07:00 or 19:00 (skip 58.9 and 65.9). Change nothing else before n>=5 per hour.
8. **Openers:** the first 1080p-source clips get a calm cinematic opener (food, water, kitchen, golden light; never harsh or gloomy). Report skip vs none at n>=5 per side. Prefer the 14 1080p episodes.

### Watch list
- **Queue depth:** nothing scheduled after 24 Oct (KT_NUTRIENTFIX 02). 25 Oct will be missed unless clips are stocked today.
- Vegan clip: 3 Instagram views vs 424 on YouTube; check if Instagram restricted it. First comment keyword or DM; first YouTube clip over 500 views.
- Fish oil clip (23 Oct) and cholesterol clip: re-read skip at 48h.
- Any third takedown (2 so far, both TikTok).
- 29 Oct review: pace, takedowns, median skip under 45% on n>=10.
