# Random Module
# -------------
# Implements pseudo-random number generators for various distributions.
# Warning: Not suitable for cryptographic purposes (use the 'secrets' module instead).

import random

# 1. Seeding
# ----------
# Setting a seed forces the random number generator to produce the exact same
# sequence of numbers every time you run the script. Great for reproducibility.
random.seed(42)

# 2. Random Numbers
# -----------------
print("--- Random Numbers ---")
print("Float between 0.0 and 1.0:", random.random())
print("Float between 2.5 and 10.0:", random.uniform(2.5, 10.0))
print("Integer between 1 and 100:", random.randint(1, 100)) # Inclusive of both endpoints
print("Even integer from 0 to 10:", random.randrange(0, 11, 2)) # start, stop, step

# 3. Operations on Sequences
# --------------------------
print("\n--- Sequence Operations ---")
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# Pick exactly one item randomly
print("Random Choice:", random.choice(fruits))

# Pick multiple items WITH replacement (can pick the same item twice)
# You can also assign weights (probabilities) to each item
print("Choices with weights:", random.choices(fruits, weights=[10, 1, 1, 1, 1], k=3))

# Pick multiple unique items WITHOUT replacement
print("Random Sample (Unique):", random.sample(fruits, k=3))

# Shuffle a list in-place
random.shuffle(fruits)
print("Shuffled List:", fruits)