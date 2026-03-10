# Functools, Lambdas, and Higher-Order Functions
# ----------------------------------------------

import functools
import time

# Lambda Functions
# Small, anonymous functions defined using the 'lambda' keyword.
# They can take any number of arguments but can only have one expression.
# Syntax: lambda arguments : expression

# Regular function
# def square(x):
#     return x * x

# Equivalent Lambda
square_lambda = lambda x: x * x
print(square_lambda(5)) # 25

add_lambda = lambda a, b: a + b
print(add_lambda(10, 20)) # 30

# map() function
# Applies a given function to all items in an input list (or any iterable).
# Syntax: map(function, iterable)

nums = [1, 2, 3, 4, 5]
# Using lambda inside map to double the numbers
doubled_nums = list(map(lambda x: x * 2, nums))
print(doubled_nums) # [2, 4, 6, 8, 10]

# filter() function
# Creates a list of elements for which a function returns True.
# Syntax: filter(function, iterable)

# Filtering out odd numbers (keeping only even ones)
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums) # [2, 4]

# functools.reduce()
# Applies a rolling computation to sequential pairs of values in a list.
# It "reduces" the list to a single value.


# Example: Multiplying all numbers in a list
# Step 1: 1 * 2 = 2
# Step 2: 2 * 3 = 6
# Step 3: 6 * 4 = 24
# Step 4: 24 * 5 = 120
product = functools.reduce(lambda x, y: x * y, nums)
print(product) # 120

# functools.partial()
# Used to "freeze" some portion of a function's arguments and keywords,
# resulting in a new object with a simplified signature.

def power(base, exp):
    return base ** exp

# We can create a dedicated 'cube' function by freezing the exp argument to 3
cube = functools.partial(power, exp=3)
print(cube(2)) # 8
print(cube(4)) # 64

# functools.lru_cache()
# A decorator that caches the return values of a function, depending on the arguments.
# It saves time when an expensive or I/O bound function is periodically called with the same arguments.

@functools.lru_cache(maxsize=None)
def expensive_fibonacci(n):
    if n < 2:
        return n
    return expensive_fibonacci(n-1) + expensive_fibonacci(n-2)

start_time = time.time()
print(expensive_fibonacci(35)) # Calculates instantly because intermediate steps are cached
print(f"Time taken: {time.time() - start_time} seconds")

# functools.wraps()
# A decorator used when building your own decorators.
# It preserves the metadata (like __name__ and docstrings) of the original function.

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling decorated function...")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """This function greets the user."""
    print(f"Hello, {name}!")

greet("Harsh")
print(greet.__name__) # Prints 'greet' (Without @wraps, it would print 'wrapper')
print(greet.__doc__)  # Prints 'This function greets the user.'