choice = 'y'

while choice =='y' or choice == 'Y' : # make 'Y' valid too
    try:
        # typecast the below 2 to a list
        
        numbers =input("Enter the input numbers separated by spaces: ").split(" ") # split the input string into a list of numbers
        operators = input("Enter operators between them: ").split(" ") # split the input string into a list of operators

        # check length matching

        if len(numbers) != 1 + len(operators): # this seems odd... u might say it's ... off by one
            print("Invalid length of numbers or operators or both inputted!! ") # replace wiht better message :)
            continue
        
        flag = True # this seems correct
        for i in range(0, len(numbers)-1): # indexing range fix
            a, b, op = int(numbers[i]), int(numbers[i+1]), operators[i]
            # correct the ops
            match op:
                case '+':
                    c = a + b
                case '-':
                    c = a - b
                case '*':
                    c = a * b
                case '/':
                    c = a / b
                case '%':
                    c = a % b
                case '//':
                    c = a // b
                case '**':
                    c = a ** b
                case _:
                    flag = False
            if not flag:
                print("Invalid ops vro")
                break

            numbers[i+1] = c
        if not flag:
            continue
        print(f"Output: {numbers[-1]}")
    except Exception:
        print(f"Exception: Error!! Division by zero ") # print exception
    finally:
        choice = input("Do you want to continue? [y/n] : ") # always ask before ending

# can you make the code shorter and with improved answer? 
# like handling any basic arithmetic equation (that may have brackets too) ?
# u might wanna find a special function in python