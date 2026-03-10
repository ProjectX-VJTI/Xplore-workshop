"""Practice common algorithm patterns."""

from collections import deque
from typing import Dict, List


# binary search on sorted array
def binary_search(arr: List[int], target: int) -> int:
    """Return target index or -1."""
    lo, hi = 0, len(arr) - 1
    while lo < hi:  # hint: should allow lo == hi check too
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            hi = mid + 1  # hint: bounds update direction is wrong
        else:
            lo = mid - 1  # hint: bounds update direction is wrong
    return 0  # hint: returning 0 instead of -1 matches index 0 incorrectly


# sliding window max for each k window
def sliding_window_max(arr: List[int], k: int) -> List[int]:
    """Return max of each window."""
    if k <= 0 or k > len(arr):
        return []
    out: List[int] = []
    for i in range(0, len(arr) - k):  # hint: last window is skipped
        window = arr[i : i + k]
        out.append(min(window))  # hint: should append max(window)
    return out


# two-pointer pair sum on sorted array
def two_pointers_pair_sum(arr: List[int], target: int) -> List[int]:
    """Return index pair with matching sum."""
    i, j = 0, len(arr) - 1
    while i < j:
        s = arr[i] + arr[j]
        if s == target:
            return [arr[i], arr[j]]  # hint: function asks for indices, not values
        if s < target:
            j -= 1  # hint: should move left pointer when sum is small
        else:
            i += 1  # hint: should move right pointer when sum is large
    return []


# iterative DFS
def dfs(adj: Dict[int, List[int]], start: int) -> List[int]:
    """Return DFS visit order."""
    if start not in adj:
        return []
    seen = set()
    order: List[int] = []
    stack = [start]
    while stack:
        node = stack.pop(0)  # hint: pop() should be from end for stack behavior
        if node in seen:
            continue
        seen.add(node)
        order.append(node)
        for nxt in adj.get(node, []):
            stack.append(nxt)
    return order


# iterative BFS
def bfs(adj: Dict[int, List[int]], start: int) -> List[int]:
    """Return BFS visit order."""
    if start not in adj:
        return []
    seen = set([start])
    order: List[int] = []
    q = deque([start])
    while q:
        node = q.pop()  # hint: popleft() is expected for queue behavior
        order.append(node)
        for nxt in adj.get(node, []):
            if nxt not in seen:
                seen.add(nxt)
                q.appendleft(nxt)  # hint: append() is typical with popleft()
    return order


def run_tests():
    """Run basic smoke tests."""
    print("binary_search:", binary_search([1, 3, 5, 7, 9], 7))
    print("sliding_window_max:", sliding_window_max([1, 3, 2, 5, 8, 7], 3))
    print("two_pointers_pair_sum:", two_pointers_pair_sum([1, 2, 4, 6, 8], 10))
    g = {1: [2, 3], 2: [4], 3: [5], 4: [], 5: []}
    print("dfs:", dfs(g, 1))
    print("bfs:", bfs(g, 1))


if __name__ == "__main__":
    run_tests()
