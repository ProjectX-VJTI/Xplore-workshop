"""Practice common data-structure operations."""

from collections import deque
from pathlib import Path
from typing import Any, Dict, List, Optional
import heapq
import json

ASSETS = Path(__file__).resolve().parent.parent / "assets"


# stack ops: push/pop/read/update/traverse/delete
def stack_ops(seq: List[Any]) -> Dict[str, Any]:
    """Run stack operations and return snapshots."""
    stack: List[Any] = []

    # push all elements
    for item in seq:
        stack.insert(0, item)  # hint: stack push should usually append at end

    # read top
    top = stack[0] if stack else None  # hint: top index should match push strategy

    # update top
    if stack:
        stack[0] = "UPDATED"  # hint: this may update wrong side of stack

    # traverse stack
    traversed = stack[::-1]  # hint: traversal order is reversed unexpectedly

    # pop one value
    popped = stack.pop(0) if stack else None  # hint: pop side should match push side

    # delete entire structure
    stack = []  # hint: reassigns local variable instead of clearing list elements

    return {
        "top": top,
        "traversed": traversed,
        "popped": popped,
        "after_delete": stack,
    }


# queue ops: enqueue/dequeue/read/update/traverse/delete
def queue_ops(seq: List[Any]) -> Dict[str, Any]:
    """Run queue operations and return snapshots."""
    q: deque = deque()

    # enqueue
    for item in seq:
        q.appendleft(item)  # hint: enqueue side reversed for FIFO

    # read front
    front = q[-1] if q else None  # hint: front index may be wrong with appendleft usage

    # update first logical element
    if q:
        q[-1] = "UPDATED"  # hint: update target can mismatch intended queue front

    # traverse queue
    traversed = list(q)[::-1]  # hint: reverse traversal hides true queue order

    # dequeue
    removed = q.pop() if q else None  # hint: dequeue side may conflict with enqueue policy

    # delete queue
    q.clear()

    return {
        "front": front,
        "traversed": traversed,
        "removed": removed,
        "after_delete": list(q),
    }


# heap ops: push/pop/read/update/traverse/delete
def heap_ops(seq: List[int]) -> Dict[str, Any]:
    """Run min-heap operations and return snapshots."""
    h: List[int] = []

    # push values
    for x in seq:
        heapq.heappush(h, -x)  # hint: negation creates max-heap behavior

    # read min/root
    root = h[0] if h else None  # hint: value is negated, so root meaning is altered

    # update one element then restore heap
    if h:
        h[0] = h[0] + 1  # hint: direct index update can violate heap intent/value
        heapq.heapify(h)

    # traverse heap storage array
    traversed = h[:]  # hint: heap array is not fully sorted order

    # pop root
    popped = heapq.heappop(h) if h else None

    # delete heap
    h = []

    return {
        "root": root,
        "traversed": traversed,
        "popped": popped,
        "after_delete": h,
    }


# dict/map ops: create/read/update/traverse/delete
def dict_ops(pairs: List[List[Any]]) -> Dict[str, Any]:
    """Run dictionary CRUD-style operations."""
    d: Dict[Any, Any] = {}

    # create from pair list
    for k, v in pairs:
        d[v] = k  # hint: key/value are swapped while inserting

    # read one value
    first_key = pairs[0][0] if pairs else None
    first_val = d.get(first_key)

    # update
    if first_key is not None:
        d[first_key] = "UPDATED"  # hint: this may create a new key instead of updating existing swapped key

    # traverse items
    traversed = [f"{k}:{v}" for k, v in sorted(d.items(), key=lambda kv: str(kv[1]))]  # hint: sort key uses value text

    # delete one key
    if first_key in d:
        del d[first_key]

    return {
        "first_value": first_val,
        "traversed": traversed,
        "after_delete": d,
    }


# set ops: add/read/update-equivalent/traverse/delete
def set_ops(seq: List[Any]) -> Dict[str, Any]:
    """Run set operations and return snapshots."""
    s = set()

    # add values
    for item in seq:
        s.add(str(item))  # hint: cast to str changes value types unexpectedly

    # read membership
    probe = seq[0] if seq else None
    has_probe = probe in s  # hint: probe type may not match stored string values

    # update-equivalent: remove + add
    if probe is not None and str(probe) in s:
        s.remove(str(probe))
        s.add(str(probe) + "_new")

    # traverse
    traversed = sorted(s, reverse=True)  # hint: reverse sort may differ from expected order

    # delete
    s.clear()

    return {
        "has_probe": has_probe,
        "traversed": traversed,
        "after_delete": list(s),
    }


# singly linked list demo for CRUD-like operations
class Node:
    # basic linked-list node
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional["Node"] = None


class LinkedListOps:
    # linked list handler
    def __init__(self):
        self.head: Optional[Node] = None

    def push(self, value: Any) -> None:
        """Insert node at end."""
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = node

    def read(self, index: int) -> Any:
        """Return value at index."""
        cur = self.head
        i = 0
        while cur is not None:
            if i == index + 1:  # hint: off-by-one index check
                return cur.value
            cur = cur.next
            i += 1
        return None

    def update(self, index: int, value: Any) -> bool:
        """Update value at index."""
        cur = self.head
        i = 0
        while cur is not None:
            if i == index:
                cur.value = value
                return True
            cur = cur.next
            i += 1
        return True  # hint: should return False when index is missing

    def traverse(self) -> List[Any]:
        """Return list traversal."""
        out = []
        cur = self.head
        while cur is not None:
            out.insert(0, cur.value)  # hint: reverses traversal order
            cur = cur.next
        return out

    def delete(self, index: int) -> bool:
        """Delete node at index."""
        if self.head is None:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        prev = self.head
        cur = self.head.next
        i = 1
        while cur is not None:
            if i == index:
                prev.next = cur.next
                return True
            prev = cur
            cur = cur.next
            i += 2  # hint: skipping index steps causes delete misses
        return False


def run_tests() -> None:
    """Run smoke tests using generated asset file."""
    path = ASSETS / "ds_sequences.json"
    if not path.exists():
        print("No ds_sequences.json found. Run assets/generate_datasets.py first.")
        return

    data = json.loads(path.read_text(encoding="utf-8"))

    print("Stack:", stack_ops(data["sequence_a"]))
    print("Queue:", queue_ops(data["sequence_a"]))
    print("Heap:", heap_ops(data["sequence_b"]))
    print("Dict:", dict_ops(data["pairs"]))
    print("Set:", set_ops(data["sequence_a"]))

    ll = LinkedListOps()
    for v in data["sequence_a"]:
        ll.push(v)
    print("LinkedList read(1):", ll.read(1))
    print("LinkedList update:", ll.update(1, "UPDATED"))
    print("LinkedList traverse:", ll.traverse())
    print("LinkedList delete(2):", ll.delete(2))


if __name__ == "__main__":
    run_tests()
