#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
移动 /rules/**/rule.md 中引用的 ../../assets/* 图片到 rule.md 同目录，
并将 Markdown/HTML 中的图片路径改为绝对根路径形式：/filename.ext

用法：
  python move_rule_assets.py
  python move_rule_assets.py --dry-run
  python move_rule_assets.py --overwrite

假设目录结构（示例）：
  rules/
    catA/
      x/
        rule.md              # 内含 ../../assets/PieGraph-Good.jpg
    assets/
      PieGraph-Good.jpg      # 真实图片位于两级上方的 assets

脚本会把 PieGraph-Good.jpg 移动到 rules/catA/x/ 下，并将 rule.md 中路径改为 /PieGraph-Good.jpg
"""

from pathlib import Path
import re
import shutil
import argparse
from typing import Set, Tuple, List

# 匹配 Markdown 图片：![alt](url "title")
MD_IMG_PATTERN = re.compile(
    r'!\[[^\]]*\]\((?P<url>[^)\s]+)(?:\s+"[^"]*")?\)'
)
# 匹配 HTML 图片：<img src="url" ...>
HTML_IMG_PATTERN = re.compile(
    r'<img[^>]+src=["\'](?P<url>[^"\']+)["\'][^>]*>',
    flags=re.IGNORECASE,
)

ASSETS_PREFIX = "../../assets/"  # 仅处理以此为前缀的相对路径


def find_asset_urls(text: str) -> Set[str]:
    """返回 rule.md 文本中以 ../../assets/ 开头的图片 URL 集合（去重）"""
    urls = set()
    for pat in (MD_IMG_PATTERN, HTML_IMG_PATTERN):
        for m in pat.finditer(text):
            url = m.group("url")
            if url.startswith(ASSETS_PREFIX):
                urls.add(url)
    return urls


def rewrite_urls(text: str) -> str:
    """把 ../../assets/xxx 改成 /xxx（保留原始语法结构）"""

    def _repl_md(m: re.Match) -> str:
        url = m.group("url")
        if url.startswith(ASSETS_PREFIX):
            new_url = "/" + Path(url).name
            return m.group(0).replace(url, new_url)
        return m.group(0)

    def _repl_html(m: re.Match) -> str:
        url = m.group("url")
        if url.startswith(ASSETS_PREFIX):
            new_url = "/" + Path(url).name
            return m.group(0).replace(url, new_url)
        return m.group(0)

    text = MD_IMG_PATTERN.sub(_repl_md, text)
    text = HTML_IMG_PATTERN.sub(_repl_html, text)
    return text


def move_assets_for_rule(rule_md: Path, urls: Set[str], dry_run: bool, overwrite: bool) -> List[Tuple[Path, Path, bool]]:
    """
    将所有匹配到的 ../../assets/* 图片移动到 rule.md 同目录。
    返回 [(src, dst, moved_bool), ...]
    """
    results = []
    # 计算该 rule.md 所在的 ../../assets 真实路径
    # 即：rule.md.parent / "../../assets"
    assets_dir = (rule_md.parent / ASSETS_PREFIX).resolve()

    for url in urls:
        filename = Path(url).name
        src = assets_dir / filename
        dst = rule_md.parent / filename

        if not src.exists():
            results.append((src, dst, False))
            continue

        if dst.exists() and not overwrite:
            # 不覆盖：视为未移动，但记录
            results.append((src, dst, False))
            continue

        if dry_run:
            # 试运行，不实际移动
            results.append((src, dst, True))
        else:
            dst_parent = dst.parent
            dst_parent.mkdir(parents=True, exist_ok=True)
            # 使用 move（若不同分区会退化为 copy+delete）
            if dst.exists() and overwrite:
                # 先删后移，避免不同平台上 move 的报错
                dst.unlink()
            shutil.move(str(src), str(dst))
            results.append((src, dst, True))

    return results


def process_rule_md(rule_md: Path, dry_run: bool, overwrite: bool) -> None:
    text = rule_md.read_text(encoding="utf-8")
    urls = find_asset_urls(text)

    if not urls:
        print(f"[SKIP] {rule_md} 未发现以 '{ASSETS_PREFIX}' 开头的图片引用。")
        return

    # 先移动文件
    move_results = move_assets_for_rule(rule_md, urls, dry_run, overwrite)

    # 再改写内容
    new_text = rewrite_urls(text)

    if new_text != text:
        if dry_run:
            print(f"[DRY] 将改写 {rule_md} 中的图片路径 -> '/<filename>' 形式")
        else:
            rule_md.write_text(new_text, encoding="utf-8")
            print(f"[OK ] 已改写图片路径：{rule_md}")

    # 打印移动结果
    for src, dst, moved in move_results:
        if not src.exists() and not moved:
            # 这里的 src.exists() 在 dry-run 下仍为 True；真实运行后若已移动则不存在
            # 但为了清晰展示，以 moved 为准
            print(f"[MISS] 源文件不存在：{src}")
            continue

        if dst.exists() and moved and not dry_run:
            print(f"[MOVE] {src} -> {dst}")
        else:
            if moved:
                print(f"[DRY] 将移动 {src} -> {dst}")
            else:
                if dst.exists() and not overwrite:
                    print(f"[SKIP] 目标已存在（未覆盖）：{dst}")
                else:
                    print(f"[SKIP] 未移动：{src} -> {dst}")


def main():
    parser = argparse.ArgumentParser(description="移动 ../../assets/* 图片到 rule.md 所在目录，并改写路径为 /filename")
    parser.add_argument("--rules-dir", type=str, default="rules", help="rules 根目录（默认：./rules）")
    parser.add_argument("--dry-run", action="store_true", help="试运行：仅打印将执行的操作，不改文件不移动")
    parser.add_argument("--overwrite", action="store_true", help="若目标已存在则覆盖（默认不覆盖）")
    args = parser.parse_args()

    rules_root = Path(args.rules_dir).resolve()
    if not rules_root.exists() or not rules_root.is_dir():
        print(f"[ERR] 未找到目录：{rules_root}")
        return

    # 递归搜索所有子目录中的 rule.md
    rule_files = list(rules_root.rglob("rule.md"))
    if not rule_files:
        print(f"[WARN] 在 {rules_root} 下未找到任何 rule.md。")
        return

    for rule_md in rule_files:
        print(f"\n=== 处理 {rule_md} ===")
        try:
            process_rule_md(rule_md, dry_run=args.dry_run, overwrite=args.overwrite)
        except Exception as e:
            print(f"[ERR] 处理 {rule_md} 失败：{e}")

    print("\n完成。")


if __name__ == "__main__":
    main()
