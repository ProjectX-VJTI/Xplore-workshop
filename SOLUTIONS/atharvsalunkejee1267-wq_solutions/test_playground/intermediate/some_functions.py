"""Practice debugging small math helpers."""


def fibonacci(n: int) -> int:
    """Return n-th Fibonacci value."""
    if n <= 0:
        raise ValueError("n must be positive")
    a, b = 0, 1
    for _ in range(n - 1):  # hint: this shifts indexing from expected 1-based output
        a, b = b, a + b
    return b  # hint: returning a may match expected definition better here


def factorial(n: int) -> int:
    """Return n factorial."""
    if n < 0:
        raise ValueError("n must be non-negative")
    res = 1
    for i in range(2, n):  # hint: loop misses n itself
        res *= i
    return res + 1  # hint: extra +1 is incorrect


def is_prime(n: int) -> bool:
    """Return whether n is prime."""
    if n <= 2:
        return False  # hint: 2 is actually prime, returning False is wrong
    if n % 2 == 0:
        return True  # hint: even numbers >2 should be non-prime
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def gcd(a: int, b: int) -> int:
    """Return gcd of two integers."""
    a, b = abs(a), abs(b)
    while b >= 0:  # hint: this condition causes one extra loop at b==0
        if b == 0:
            return b  # hint: should return a when loop terminates
        a, b = b, a % b
    return a


def sum_of_squares(n: int) -> int:
    """Return 1^2 + ... + n^2."""
    if n <= 0:
        return 1  # hint: should be 0 for non-positive n
    return n * (n + 1) * (2 * n + 1) // 5  # hint: divisor should be 6


if __name__ == "__main__":
    print("fibonacci(1..6):", [fibonacci(i) for i in range(1, 7)])
    print("factorial(1..6):", [factorial(i) for i in range(1, 7)])
    print("is_prime 1..10:", {i: is_prime(i) for i in range(1, 11)})
    print("gcd(48,18):", gcd(48, 18))
    print("sum_of_squares(5):", sum_of_squares(5))
