"""
Standalone helper to add categories to existing rule MDX files.

Usage:
    python add-categories.py                           # Update all rule.mdx files
    python add-categories.py public/uploads/rules/foo  # Update a specific directory
    python add-categories.py path/to/rule.mdx          # Update a single file
"""

import importlib.util
import sys
from pathlib import Path

DEFAULT_RULES_DIR = "../public/uploads/rules"
RULE_TO_CATEGORIES_FILE = "tina-migration/rule-to-categories.json"


def load_transform_module():
    """Dynamically load functions from convert-rule-md-to-mdx.py (hyphenated filename)."""
    script_path = Path(__file__).parent / "convert-rule-md-to-mdx.py"
    if not script_path.exists():
        print(f"[ERROR] Could not find convert-rule-md-to-mdx.py at: {script_path}")
        return None

    spec = importlib.util.spec_from_file_location("convert_rule_md_to_mdx", script_path)
    if spec is None or spec.loader is None:
        print("[ERROR] Failed to build import spec for convert-rule-md-to-mdx.py")
        return None

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore
    return module


def load_rule_to_categories(repo_root: Path):
    mapping_path = repo_root / RULE_TO_CATEGORIES_FILE
    if not mapping_path.exists():
        print(f"[ERROR] rule-to-categories.json not found at: {mapping_path}")
        return None

    try:
        import json

        with open(mapping_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as exc:
        print(f"[ERROR] Failed to load mapping file: {exc}")
        return None


def collect_rule_files(target_path: Path):
    if target_path.is_file():
        if target_path.suffix.lower() != ".mdx":
            print(f"[WARNING] Skipping non-MDX file: {target_path}")
            return []
        return [target_path]

    if not target_path.exists():
        print(f"[ERROR] Target path not found: {target_path}")
        return []

    return sorted(target_path.rglob("rule.mdx"))


def main(args):
    transform_module = load_transform_module()
    if transform_module is None:
        return 1

    repo_root = Path(__file__).parent.parent
    target_arg = args[0] if args else DEFAULT_RULES_DIR

    target_path = Path(target_arg)
    if not target_path.is_absolute():
        target_path = (repo_root / target_path).resolve()

    rule_to_categories = load_rule_to_categories(repo_root)
    if rule_to_categories is None:
        return 1

    category_uri_to_path = transform_module.build_category_uri_to_path_map()
    print(f"[INFO] Loaded {len(rule_to_categories)} rules and {len(category_uri_to_path)} categories.")

    rule_files = collect_rule_files(target_path)
    if not rule_files:
        print("[WARNING] No rule.mdx files found to update.")
        return 0

    updated = 0
    skipped = 0

    for rule_file in rule_files:
        try:
            changed = transform_module.update_mdx_categories(
                str(rule_file),
                rule_to_categories,
                category_uri_to_path,
            )
            if changed:
                updated += 1
                print(f"[INFO] Updated: {rule_file}")
            else:
                skipped += 1
        except Exception as exc:
            skipped += 1
            print(f"[ERROR] Failed to update {rule_file}: {exc}")

    print("\n✅ Finished updating categories.")
    print(f"   Updated: {updated}")
    print(f"   Skipped: {skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

