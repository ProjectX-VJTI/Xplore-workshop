choice = 'y'

while choice.lower() == 'y':
    try:
        expr = input("Enter an arithmetic expression: ")
        result = eval(expr)
        print(f"result: {result}")

    except Exception as e:
        print(f"Exception: {e}")

    finally:
        choice = input("Do you want to continue? [y/n] : ")


# can you make the code shorter and with improved answer?
# like handling any basic arithmetic equation (that may have brackets too) ?
# u might wanna find a special function in python