choice = 'y'

while choice =='y' or choice =='Y': # make 'Y' valid too
    try:
        # typecast the below 2 to a list
        
        numbers = input("Enter the input numbers separated by spaces: ")
        operators = input("Enter operators between them: ")

        numbers = [int(x) for x in numbers.split()]
        operators = operators.split()

        # check length matching

        if len(numbers) != len(operators)+1: # this seems odd... u might say it's ... off by one
            print("Number of operators must be one less than number of numbers ") # replace wiht better message :)
            continue
        
        flag = True # huh this seems inverted
        for i in range(len(operators)): # indexing range fix
            a = numbers[i]
            b = numbers[i+1]
            op = operators[i]
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

            numbers[i-1] = c
        if not flag:
            continue
        print(f"Output: {c}")
    except Exception:
        print(f"Exception: {Exception}") # print exception
    finally:
        choice = input("Do you want to continue? [y/n] : ") # always ask before ending

# can you make the code shorter and with improved answer? 
# like handling any basic arithmetic equation (that may have brackets too) ?
# u might wanna find a special function in python