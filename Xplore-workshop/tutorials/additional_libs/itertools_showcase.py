# Itertools Module
# ----------------
# A collection of fast, memory-efficient tools for creating and handling iterators.

import itertools
import operator

# 1. Combinatoric Iterators
# Used to generate combinations, permutations, and Cartesian products.

# itertools.permutations()
# Returns all possible orderings of an input iterable.
# Order matters: (A, B) is different from (B, A)

letters = ['A', 'B', 'C']
perms = list(itertools.permutations(letters, 2)) # Length of 2
print("Permutations of 2:")
print(perms) 
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# itertools.combinations()
# Returns all possible combinations of an input iterable.
# Order does NOT matter: (A, B) is the same as (B, A), so only one is returned.

combs = list(itertools.combinations(letters, 2))
print("Combinations of 2:")
print(combs)
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

# itertools.product()
# Computes the Cartesian product of input iterables. 
# Equivalent to nested for-loops.

colors = ['Red', 'Blue']
sizes = ['S', 'M']
prod = list(itertools.product(colors, sizes))
print("Cartesian Product:")
print(prod)
# [('Red', 'S'), ('Red', 'M'), ('Blue', 'S'), ('Blue', 'M')]

# 2. Terminating Iterators
# Iterators that stop at the shortest input iterable.

# itertools.chain()
# Takes several iterables and chains them together into one continuous sequence.

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
chained = list(itertools.chain(list1, list2))
print("Chained Lists:")
print(chained)
# [1, 2, 3, 'a', 'b', 'c']

# itertools.accumulate()
# Makes an iterator that returns accumulated sums (or other accumulated results like min/max).

numbers = [1, 2, 3, 4, 5]
# Default is running sum
running_sum = list(itertools.accumulate(numbers))
print("Running Sum:")
print(running_sum) # [1, 3, 6, 10, 15]

# Using a different operator (e.g., multiplication)
running_product = list(itertools.accumulate(numbers, operator.mul))
print("Running Product:")
print(running_product) # [1, 2, 6, 24, 120]

# itertools.compress()
# Filters elements from data returning only those that have a corresponding True in selectors.

data = ['Apple', 'Banana', 'Cherry', 'Dates']
selectors = [True, False, True, False]
compressed = list(itertools.compress(data, selectors))
print("Compressed Data:")
print(compressed) # ['Apple', 'Cherry']

# 3. Infinite Iterators
# Iterators that go on forever (use with caution, usually paired with a break condition or islice).

# itertools.count(start, step)
# Starts at a number and keeps adding the step value.

print("Count Example:")
for i in itertools.count(10, 5):
    if i > 30:
        break
    print(i, end=" ") # 10 15 20 25 30
print()

# itertools.cycle(iterable)
# Cycles through an iterable infinitely.

print("Cycle Example:")
counter = 0
for item in itertools.cycle(['ON', 'OFF']):
    if counter > 4:
        break
    print(item, end=" ") # ON OFF ON OFF ON
    counter += 1
print()