# Collections Module
# ------------------
# Provides specialized container datatypes acting as alternatives to 
# Python's general-purpose built-in containers (dict, list, set, and tuple).

import collections

# 1. Counter
# A dict subclass for counting hashable objects. 
# Elements are stored as dictionary keys and their counts are stored as values.

freq = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
print("Counter Dictionary:")
print(freq)                 # Counter({'b': 3, 'a': 2, 'c': 1})
print(freq['b'])            # 3

# Most common elements
print(freq.most_common(1))  # [('b', 3)]

# 2. namedtuple
# Factory function for creating tuple subclasses with named fields.
# Makes code cleaner by avoiding integer indexes.

# Create a class-like blueprint called 'Point'
Point = collections.namedtuple('Point', ['x', 'y'])
p1 = Point(10, 20)

print("\nNamedTuple Point:")
print(p1)                   # Point(x=10, y=20)
print(p1.x, p1.y)           # 10 20 (Accessed by name instead of p1[0])

# 3. defaultdict
# A dict subclass that calls a factory function to supply missing values.
# Prevents KeyError when trying to access or modify a key that doesn't exist yet.

# Using list as the default_factory
dd = collections.defaultdict(list)
dd['fruits'].append('apple')
dd['fruits'].append('banana')

print("\nDefaultDict:")
print(dd)                   # defaultdict(<class 'list'>, {'fruits': ['apple', 'banana']})
print(dd['veggies'])        # [] (Automatically creates an empty list for missing key)

# 4. deque (Double-Ended Queue)
# A list-like container with fast appends and pops on either end.
# Lists are slow for inserting/popping at the beginning (O(n)), but deques are fast (O(1)).

dq = collections.deque([1, 2, 3])
dq.append(4)                # Add to the right
dq.appendleft(0)            # Add to the left

print("\nDeque Operations:")
print(dq)                   # deque([0, 1, 2, 3, 4])

dq.pop()                    # Remove from the right
dq.popleft()                # Remove from the left
print(dq)                   # deque([1, 2, 3])