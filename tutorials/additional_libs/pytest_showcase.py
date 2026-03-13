# Testing in Python: unittest and pytest
# --------------------------------------
# This file contains the logic to be tested and the test suites.

import unittest

# --- 1. The Logic (Code to be tested) ---

class Calculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def divide(self, a, b):
        if b == 0: raise ValueError("Cannot divide by zero")
        return a / b

def fibonacci(n):
    if n <= 0: return []
    if n == 1: return [0]
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

def tribonacci(n):
    if n <= 0: return []
    if n == 1: return [0]
    if n == 2: return [0, 1]
    seq = [0, 1, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2] + seq[-3])
    return seq

def sum_all(*args): return sum(args)

def product_all(*args):
    res = 1
    for x in args: res *= x
    return res

# --- 2. Unittest Showcase (Built-in) ---

class TestAlgebra(unittest.TestCase):
    def test_calculator(self):
        calc = Calculator()
        self.assertEqual(calc.add(10, 5), 15)
        self.assertRaises(ValueError, calc.divide, 10, 0)

    def test_sequences(self):
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(tribonacci(5), [0, 1, 1, 2, 4])

# --- 3. Pytest Showcase (Modern) ---
# Note: To run these via pytest, you would normally run 'pytest pytest_showcase.py' in terminal.
# Pytest uses simple 'assert' statements.

def test_math_utils():
    assert sum_all(1, 2, 3) == 6
    assert product_all(2, 3, 4) == 24
    assert fibonacci(1) == [0]

if __name__ == "__main__":
    # Running the unittest suite
    print("Running Unittest Suite...")
    unittest.main(exit=False)