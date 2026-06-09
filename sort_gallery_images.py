#!/usr/bin/env python3
"""
Run this script inside your fps_gallery_images folder.
It reads each filename and moves it into a matching project subfolder.
Usage: python3 sort_gallery_images.py
"""
import os, shutil, re

GROUPS = {
    "bronxville-luxury":    ["bronxville", "luxury", "apartment", "kitchen", "marble", "vanity", "shower", "closet", "hallway", "living", "staged"],
    "supportive-housing":   ["supportive", "housing", "unit", "kitchenette", "bedroom", "bathroom", "parapet", "coping", "skyline", "rehab", "55"],
    "masonry-entrance":     ["masonry", "entrance", "stoop", "brick", "facade", "pointing", "brownstone", "before", "after"],
    "roof-waterproofing":   ["roof", "roofing", "waterproof", "membrane", "coating", "terrace", "deck", "flat"],
    "commercial":           ["commercial", "office", "lobby", "retail", "store", "storefront"],
    "mechanical":           ["mechanical", "hvac", "plumbing", "boiler", "pipe", "sprinkler"],
}

def best_group(filename):
    name = filename.lower()
    scores = {g: 0 for g in GROUPS}
    for group, keywords in GROUPS.items():
        for kw in keywords:
            if kw in name:
                scores[group] += 1
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "uncategorized"

folder = "."
images = [f for f in os.listdir(folder)
          if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".webp"))
          and os.path.isfile(os.path.join(folder, f))]

if not images:
    print("No images found in current folder. Run this script inside fps_gallery_images/")
    exit()

moved = {}
for img in images:
    group = best_group(img)
    dest_dir = os.path.join(folder, group)
    os.makedirs(dest_dir, exist_ok=True)
    shutil.move(os.path.join(folder, img), os.path.join(dest_dir, img))
    moved.setdefault(group, []).append(img)

print("\n=== Sorted Results ===")
for group, files in sorted(moved.items()):
    print(f"\n📁 {group}/ ({len(files)} images)")
    for f in files:
        print(f"   {f}")

uncategorized = moved.get("uncategorized", [])
if uncategorized:
    print(f"\n⚠️  {len(uncategorized)} images couldn't be auto-matched — check 'uncategorized/' folder and move manually.")
print("\nDone! Now drag each subfolder into GitHub under images/projects/")
