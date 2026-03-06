# Math Module
# -----------
# Provides access to the mathematical functions defined by the C standard.
# Note: These functions cannot be used with complex numbers (use the 'cmath' module for that).

import math

# 1. Constants
# ------------
print("--- Constants ---")
print("Pi:", math.pi)            # 3.141592653589793
print("Euler's Number (e):", math.e) # 2.718281828459045
print("Infinity:", math.inf)     # Positive infinity
print("Not a Number:", math.nan) # NaN (Not a Number)

# 2. Number Representation & Rounding
# -----------------------------------
print("\n--- Rounding & Representation ---")
num = 4.7

print("Original Number:", num)
print("Ceil (Round up):", math.ceil(num))     # 5
print("Floor (Round down):", math.floor(num)) # 4
print("Truncate (Remove decimal):", math.trunc(num)) # 4

# math.isclose() is crucial for comparing floating-point numbers due to precision issues
print("0.1 + 0.2 == 0.3?", 0.1 + 0.2 == 0.3)  # False!
print("Is close?", math.isclose(0.1 + 0.2, 0.3)) # True

# 3. Power & Logarithmic Functions
# --------------------------------
print("\n--- Powers & Logs ---")
print("Square Root of 16:", math.sqrt(16))    # 4.0
print("2 to the power of 3:", math.pow(2, 3)) # 8.0 (Returns float, unlike 2**3)
print("e^2:", math.exp(2))                    # e squared
print("Natural Log of e:", math.log(math.e))  # 1.0 (Base e by default)
print("Log base 10 of 100:", math.log10(100)) # 2.0

# 4. Trigonometry
# ---------------
print("\n--- Trigonometry ---")
# Math trig functions expect radians, not degrees.
angle_degrees = 90
angle_radians = math.radians(angle_degrees)

print(f"{angle_degrees} degrees in radians:", angle_radians)
print("Sine of 90 degrees:", math.sin(angle_radians)) # 1.0
print("Cosine of 90 degrees:", math.cos(angle_radians)) # Very close to 0