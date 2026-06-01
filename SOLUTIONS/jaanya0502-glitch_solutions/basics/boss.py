choice = 'y'

while choice == 'y' or choice == 'Y':  # make 'Y' valid too
    try:
        # typecast the below 2 to a list

        numbers = list(input("Enter the input numbers separated by spaces: ").split())
        numbers = [int(x) for x in numbers]
        operators = list(input("Enter operators between them: ").split())

        # check length matching
        print(type(numbers[0]))
        if len(numbers) - 1 != len(operators):
            print("Invalid syntax")
            continue

        flag = True  # huh this seems inverted
        for i in range(1, len(numbers)):  # indexing range fix
            a, b, op = numbers[i - 1], numbers[i], operators[i - 1]

            # correct the ops
            if op == '+':
             c = a + b
            elif op == '-':
             c = a - b
            elif op == '*':
              c = a * b
            elif op == '/':
                c = a / b
            elif op == '%':
             c = a % b
            elif op == '//':
              c = a // b
            elif op == '**':
                    c = a ** b
            else:
             flag = False
            if not flag:
                print("Invalid ops vro")
                break

            numbers[i] = c

        if not flag:
            continue

        print("Output:", numbers[-1])

    except Exception as e:
        print("Exception:", e)

    finally:
        choice = input("Do you want to continue? [y/n] : ")

# can you make the code shorter and with improved answer? 
# like handling any basic arithmetic equation (that may have brackets too) ?
# u might wanna find a special function in python

        choice = 'y'

while choice.lower() == 'y':
    try:
        expr = input("Enter expression: ")
        result = eval(expr)
        print("Output:", result)

    except Exception as e:
        print("Error:", e)

    choice = input("Do you want to continue? [y/n]: ")