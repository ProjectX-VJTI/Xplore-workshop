"""Practice debugging small math helpers."""


def fibonacci(n: int) -> int:
    """Return n-th Fibonacci value (1-based: 1, 1, 2, 3, 5...)."""
    if n <= 0:
        raise ValueError("n must be positive")
    a, b = 0, 1
    # To get the n-th number in the sequence 1, 1, 2, 3...
    # we loop n-1 times and return b.
    for _ in range(n - 1):
        a, b = b, a + b
    return b 


def factorial(n: int) -> int:
    """Return n factorial (n!)."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0 or n == 1:
        return 1
    res = 1
    # range(2, n + 1) ensures we include n in the multiplication
    for i in range(2, n + 1):
        res *= i
    return res 


def is_prime(n: int) -> bool:
    """Return whether n is prime."""
    if n < 2:
        return False
    if n == 2:
        return True  # 2 is the only even prime number!
    if n % 2 == 0:
        return False # Even numbers > 2 are never prime
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def gcd(a: int, b: int) -> int:
    """Return greatest common divisor using Euclidean Algorithm."""
    a, b = abs(a), abs(b)
    while b > 0: # Loop should stop exactly when b becomes 0
        a, b = b, a % b
    return a # When b is 0, a holds the GCD


def sum_of_squares(n: int) -> int:
    """Return 1^2 + ... + n^2 using the formula."""
    if n <= 0:
        return 0 
    # The correct mathematical formula is [n(n+1)(2n+1)] / 6
    return n * (n + 1) * (2 * n + 1) // 6 


if __name__ == "__main__":
    # Test cases to verify the fixes
    print("fibonacci(1..6):", [fibonacci(i) for i in range(1, 7)]) 
    print("factorial(1..6):", [factorial(i) for i in range(1, 7)]) 
    print("is_prime 1..10:", {i: is_prime(i) for i in range(1, 11)})
    print("gcd(48,18):", gcd(48, 18)) 
    print("sum_of_squares(5):", sum_of_squares(5)) 
