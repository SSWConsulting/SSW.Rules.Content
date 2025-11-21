import json
import requests
import time
from urllib.parse import urljoin
from pathlib import Path

BASE_URL = "https://www.ssw.com.au/rules-beta"
REDIRECTS_FILE = Path("scripts/tina-migration/redirects.json")
REPORT_FILE = Path("scripts/tina-migration/redirect-report.json")

TIMEOUT = 20

def normalize_url(url: str) -> str:
    return url.rstrip("/")

def check_redirect(old_path: str, new_path: str):
    old_url = urljoin(BASE_URL + "/", old_path)
    expected_new_url = urljoin(BASE_URL + "/", new_path)

    try:
        resp = requests.get(old_url, allow_redirects=True, timeout=TIMEOUT)
        final_url = resp.url

        ok = resp.ok and normalize_url(final_url) == normalize_url(expected_new_url)

        return {
            "old_url": old_url,
            "expected_new_url": expected_new_url,
            "status_code": resp.status_code,
            "final_url": final_url,
            "ok": ok,
            "error": None,
        }
    except requests.RequestException as e:
        return {
            "old_url": old_url,
            "expected_new_url": expected_new_url,
            "status_code": None,
            "final_url": None,
            "ok": False,
            "error": str(e),
        }

def main():
    start = time.perf_counter()
    data = json.loads(REDIRECTS_FILE.read_text(encoding="utf-8"))

    results = []

    for i, (old_path, new_path) in enumerate(data.items(), start=1):
        result = check_redirect(old_path, new_path)
        results.append(result)

        mark = "✅" if result["ok"] else "❌"
        print(
            f"{i:4d}. {mark} {old_path} -> {new_path} | "
            f"status={result['status_code']} | "
            f"final={result['final_url'] or 'N/A'}"
        )

    failed = [r for r in results if not r["ok"]]

    print("\n==== SUMMARY ====")
    print(f"Total:  {len(results)}")
    print(f"Passed: {len(results) - len(failed)}")
    print(f"Failed: {len(failed)}")

    if failed:
        print("\nFailed redirects:")
        for r in failed:
            print(
                f"- {r['old_url']} -> {r['expected_new_url']}, "
                f"status={r['status_code']}, final={r['final_url']}, error={r['error']}"
            )

    minimal_failed = [
        {
            "old_url": r["old_url"],
            "expected_new_url": r["expected_new_url"],
            "status_code": r["status_code"],
            "final_url": r["final_url"],
            "error": r["error"],
        }
        for r in failed
    ]

    REPORT_FILE.write_text(json.dumps(minimal_failed, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nFailed redirects have been saved to {REPORT_FILE}")

    end = time.perf_counter()
    print(f"\nTotal time: {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
