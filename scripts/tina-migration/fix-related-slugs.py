#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fix and normalize `related` in rule.mdx files under public/uploads/rules.

- Build slug index (uri + redirects) -> canonical uri
- Write related as a list of objects: [{ rule: "public/uploads/rules/<uri>/rule.mdx" }, ...]
  (so each item is a mapping, not a string)
- Remove `related:` if it's empty or null
- Overwrite files directly (no backups)
"""

from pathlib import Path
import re
import frontmatter

ROOT = Path("public/uploads/rules")
RULE_PATH_RE = re.compile(r"public/uploads/rules/([^/\s]+)/rule\.mdx$", re.IGNORECASE)

def normalize(slug: str) -> str:
    s = (slug or "").strip().lower().strip("/")
    s = re.sub(r"\s+", "-", s)
    s = s.replace("_", "-")
    return s

def collect_rule_files(root: Path):
    return sorted(root.rglob("rule.mdx"))

def build_slug_index(files):
    slug_to_canonical = {}
    conflicts = {}

    for path in files:
        try:
            post = frontmatter.load(path)
        except Exception:
            continue

        uri = post.get("uri")
        if not uri:
            continue

        canonical = normalize(uri)
        slugs = {canonical}
        for r in (post.get("redirects") or []):
            if r:
                slugs.add(normalize(r))

        for s in slugs:
            prev = slug_to_canonical.get(s)
            if prev is None:
                slug_to_canonical[s] = canonical
            elif prev != canonical:
                conflicts.setdefault(s, set()).update([prev, canonical])

    return slug_to_canonical, conflicts

def extract_slug(item) -> str:
    # support dict item: {"rule": "public/uploads/rules/<slug>/rule.mdx"}
    if isinstance(item, dict) and "rule" in item:
        s = str(item.get("rule") or "").strip()
    else:
        s = str(item or "").strip()

    if s.lower().startswith("rule:"):
        after = s.split(":", 1)[1].strip()
        m = RULE_PATH_RE.search(after)
        if m:
            return normalize(m.group(1))
        return normalize(after)
    return normalize(s)

def make_rule_obj(slug: str) -> dict:
    return {"rule": f"public/uploads/rules/{slug}/rule.mdx"}

def fix_related(path: Path, slug_map, conflicts):
    post = frontmatter.load(path)
    related = post.get("related")

    # remove if None/empty
    if not related:
        if "related" in post:
            del post["related"]
            path.write_text(frontmatter.dumps(post), encoding="utf-8")
            print(f"[removed empty] {path}")
            return True
        return False

    if not isinstance(related, list):
        return False

    old_related = related[:]  # may contain strings or dicts
    new_related = []

    for item in old_related:
        slug = extract_slug(item)
        if slug in slug_map and slug not in conflicts:
            slug = slug_map[slug]
        new_related.append(make_rule_obj(slug))  # object, not string

    changed = (new_related != old_related)
    if changed:
        post["related"] = new_related
        path.write_text(frontmatter.dumps(post), encoding="utf-8")
        print(f"[updated] {path}")
    return changed

def main():
    files = collect_rule_files(ROOT)
    if not files:
        print(f"No rule.mdx files found under {ROOT}")
        return

    slug_map, conflicts = build_slug_index(files)
    print(f"Slug mappings: {len(slug_map)}, conflicts: {len(conflicts)}")

    updated = 0
    removed_empty = 0

    for p in files:
        try:
            before = p.read_text(encoding="utf-8")
            changed = fix_related(p, slug_map, conflicts)
            after = p.read_text(encoding="utf-8")
            if changed:
                updated += 1
                if "related:" not in after and "related:" in before:
                    removed_empty += 1
        except Exception as e:
            print(f"[error] {p}: {e}")

    print(f"Done. Updated {updated} files (removed empty related: {removed_empty}).")

if __name__ == "__main__":
    main()
