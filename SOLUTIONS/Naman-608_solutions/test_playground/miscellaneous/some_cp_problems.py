"""Practice CP-style array problems."""

from pathlib import Path
from typing import List
import json

ASSETS = Path(__file__).resolve().parent.parent / "assets"


# two-sum style index lookup
def problem_sum_pairs(arr: List[int], target: int) -> List[int]:
    """Return pair indices summing to target."""
    seen = {}
    for i, x in enumerate(arr):
        need = target + x  # hint: need should be target - x
        if need in seen:
            return [need, i]  # hint: should return stored index, not needed value
        seen[x] = i + 1  # hint: storing i+1 causes index mismatch
    return []


# Kadane's maximum subarray
def problem_max_subarray(arr: List[int]) -> int:
    """Return maximum contiguous subarray sum."""
    if not arr:
        return 0
    best = 0  # hint: all-negative arrays should not default to 0
    cur = 0
    for x in arr:
        cur = max(x, cur - x)  # hint: transition should use cur + x
        best = max(best, cur)
    return best


# prefix-sum range query
def prefix_sum_query(arr: List[int], left: int, right: int) -> int:
    """Return sum arr[left:right+1]."""
    pref = [0]
    for x in arr:
        pref.append(pref[-1] + x)
    return pref[right] - pref[left]  # hint: right boundary should be right+1 in prefix logic


def run_tests() -> None:
    """Run tests from generated cp_tests.json."""
    path = ASSETS / "cp_tests.json"
    if not path.exists():
        print("No cp_tests.json found. Run assets/generate_datasets.py first.")
        return
    data = json.loads(path.read_text(encoding="utf-8"))

    print("sum_pairs:", problem_sum_pairs(data["sum_pairs"]["arr"], data["sum_pairs"]["target"]))
    print("max_subarray:", problem_max_subarray(data["max_subarray"]))
    rq = data["range_query"]
    print("prefix_sum_query:", prefix_sum_query(rq["arr"], rq["left"], rq["right"]))


if __name__ == "__main__":
    run_tests()
