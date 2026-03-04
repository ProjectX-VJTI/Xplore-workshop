choice = 'y'

while choice in ('y', 'Y'): # make 'Y' valid too
    try:
        expr = input("Enter arithmetic expression: ").strip()
        if not expr:
            print("Please enter a valid expression.")
            continue

        # Safe-ish eval for educational use: no builtins, only arithmetic expression support.
        result = eval(expr, {"__builtins__": {}}, {})
        print(f"Output: {result}")
    except Exception as e:
        print(f"Exception: {e}")
    finally:
        choice = input("Do you want to continue? [y/n] : ") # always ask before ending

# can you make the code shorter and with improved answer? 
# like handling any basic arithmetic equation (that may have brackets too) ?
# u might wanna find a special function in python
