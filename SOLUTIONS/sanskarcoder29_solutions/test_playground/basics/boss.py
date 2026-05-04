expr = input("Enter arithmetic expression: ")

try:
    result = eval(expr)
    print(f"Output: {result}")
except Exception as e:
    print("Invalid expression")