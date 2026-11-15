#!/usr/bin/env python3
"""THE FREE-EBOOK END CARD ON THE CLIPS IT BELONGS TO (14 Nov 2026).

Kamay: the card (factory/endcards/wb_ebook_endcard.png: GET THE FREE EBOOK / Comment "EBOOK")
closes a clip; he accepts the book's own cover there; the word on that cover never goes into a
description. It goes ONLY on a clip whose caption gets the EBOOK ask (my_brand/offers.json
"ebook" "match" - the same test the poster uses), because a card may only promise what a
comment really gets: our bot answers EBOOK on Instagram and Facebook.
  - YouTube: nothing answers a comment there, so YouTube keeps the clip WITHOUT the card
    (the card-less file is kept as the __yt59 cut when the clip had none).
  - TikTok: a clip carrying the card never goes to the TikTok inbox (poster.tiktok_risk).
Runs in queue.py after the last gate, on the file in the posting folder. Any failure leaves
the clip exactly as it was.

    python factory/endcard.py clip.mp4 "caption text"      # try it on one file
"""
import json
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CARD = os.path.join(HERE, "endcards", "wb_ebook_endcard.png")
OFFERS = os.path.join(ROOT, "my_brand", "offers.json")
K = os.path.expanduser("~/Kamay")
FF = os.path.join(K, "bin", "ffmpeg") if os.path.exists(os.path.join(K, "bin", "ffmpeg")) else "ffmpeg"
SECS = 3.5
PIC_H = 608                      # the wide picture's window in the standard look (kt_render ARCH_PIC_H)


def wanted(caption):
    try:
        eb = json.load(open(OFFERS)).get("ebook") or {}
        return bool(eb.get("match") and os.path.exists(CARD) and re.search(eb["match"], caption or "", re.I))
    except (OSError, ValueError, re.error):
        return False


def _secs(path):
    r = subprocess.run([FF, "-hide_banner", "-i", path], capture_output=True, text=True)
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r.stderr)
    return int(m[1]) * 3600 + int(m[2]) * 60 + float(m[3]) if m else 0.0


def attach(path, caption):
    """True when the card was added. The clip keeps its name."""
    if not wanted(caption) or "__" in os.path.basename(path):
        return False
    d0 = _secs(path)
    if d0 < 5:
        return False
    stem = path[:-4]
    tmp = stem + ".card.mp4"
    y = (1920 - PIC_H) // 2
    graph = (f"[0:v]scale=1080:1920,setsar=1,fps=30,format=yuv420p[v0];"
             f"[1:v]scale=1080:{PIC_H}:flags=lanczos,pad=1080:1920:0:{y}:black,setsar=1,fps=30,format=yuv420p,"
             f"fade=t=in:st=0:d=0.3[v1];"
             f"[0:a]aresample=48000,aformat=channel_layouts=stereo[a0];"
             f"[v0][a0][v1][2:a]concat=n=2:v=1:a=1[v][a]")
    r = subprocess.run([FF, "-y", "-loglevel", "error", "-i", path, "-loop", "1", "-framerate", "30", "-t", str(SECS), "-i", CARD,
                        "-f", "lavfi", "-t", str(SECS), "-i", "anullsrc=r=48000:cl=stereo",
                        "-filter_complex", graph, "-map", "[v]", "-map", "[a]", "-r", "30",
                        "-c:v", "libx264", "-preset", "medium", "-crf", "17", "-pix_fmt", "yuv420p",
                        "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", tmp], capture_output=True, text=True)
    d1 = _secs(tmp) if r.returncode == 0 and os.path.exists(tmp) else 0.0
    if abs(d1 - d0 - SECS) > 0.4:                       # read it back: the old clip plus the card, nothing else
        print(f"  end card NOT added to {os.path.basename(path)}: {r.stderr[-200:] or f'{d0:.1f}s -> {d1:.1f}s'}")
        if os.path.exists(tmp):
            os.remove(tmp)
        return False
    if not os.path.exists(stem + "__yt59.mp4") and d0 <= 59.5:
        shutil.copy(path, stem + "__yt59.mp4")          # YouTube's copy: no card (no one answers a comment there)
    os.replace(tmp, path)
    print(f"  end card added to {os.path.basename(path)} ({d0:.1f}s -> {d1:.1f}s); YouTube keeps the clip without it")
    return True


if __name__ == "__main__":
    print(attach(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else ""))
