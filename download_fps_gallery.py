#!/usr/bin/env python3
"""
Download all gallery images from fpscontracting.com.

RUN THIS ON YOUR OWN COMPUTER (not in the Claude sandbox, which is firewalled).
  1.  pip install requests
  2.  python3 download_fps_gallery.py
It saves everything into ./fps_gallery_images/  — then drag that folder
into the chat (or commit it) and the images get grouped into projects.
"""
import os, re, sys
from urllib.parse import urljoin
import requests

BASE  = "https://fpscontracting.com"
PAGES = ["/gallery.html", "/projects.html", "/index.html", "/services.html"]
OUT   = "fps_gallery_images"
os.makedirs(OUT, exist_ok=True)

sess = requests.Session()
sess.headers.update({"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"})

found = set()
for path in PAGES:
    url = urljoin(BASE, path)
    try:
        r = sess.get(url, timeout=20)
        print(f"GET {url} -> {r.status_code}")
        if r.status_code != 200:
            continue
    except Exception as e:
        print(f"GET {url} -> FAILED ({e})")
        continue
    # <img src>, href, data-src, srcset, and CSS background-image:url(...)
    for m in re.findall(r'(?:src|href|data-src|data-original)=["\']([^"\']+\.(?:jpe?g|png|webp|gif))["\']', r.text, re.I):
        found.add(m)
    for m in re.findall(r'url\(["\']?([^"\')]+\.(?:jpe?g|png|webp))["\']?\)', r.text, re.I):
        found.add(m)
    for m in re.findall(r'(/share/images/galleries/[^\s"\'<>]+)', r.text, re.I):
        found.add(m)

urls = sorted({urljoin(BASE, u) for u in found if "logo" not in u.lower()})
print(f"\nFound {len(urls)} candidate images\n")

ok = 0
for u in urls:
    name = os.path.basename(u.split("?")[0]).replace("%20", "_")
    dest = os.path.join(OUT, name)
    try:
        ir = sess.get(u, timeout=20)
        if ir.status_code == 200 and len(ir.content) > 1024:
            with open(dest, "wb") as f:
                f.write(ir.content)
            ok += 1
            print(f"  ✓ {name}  ({len(ir.content)//1024} KB)")
        else:
            print(f"  · skip {name} (HTTP {ir.status_code}, {len(ir.content)}B)")
    except Exception as e:
        print(f"  · skip {name} ({e})")

print(f"\nDone — {ok} images saved to ./{OUT}/")
print("Now drag that folder into the Claude chat, or commit & push it.")
