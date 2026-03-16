while True:
    try:
        expr = input("Enter an arithmetic expression: ")
        result = eval(expr)
        print("Output:", result)

    except Exception as e:
        print("Error:", e)

    choice = input("Do you want to continue? [y/n]: ")
    if choice != 'y' or choice != 'Y':
        break