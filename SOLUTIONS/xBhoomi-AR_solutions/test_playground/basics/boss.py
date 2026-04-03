choice = 'y'

while choice =='y' or choice =='Y' : # make 'Y' valid too
    try:
        # typecast the below 2 to a list
        
        numbers = [int(x) for x in input("Enter the input numbers separated by spaces: ").split()]  
        operators = input("Enter operators between them: ").split() 

        # check length matching

        if len(numbers) - 1 != len(operators) : # this seems odd... u might say it's ... off by one
            print("Operation (Mission) Impossible") # replace wiht better message :)
            continue
        
        flag = True # huh this seems inverted
        for i in range(0, len(numbers)-1): # indexing range fix
            a, b, op = numbers[i], numbers[i+1], operators[i]
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
    except Exception as error:
        print(f"Exception: {error}") # print exception
    finally:
        choice = input("Do you want to continue? [y/n] : ") # always ask before ending

# can you make the code shorter and with improved answer? 
# like handling any basic arithmetic equation (that may have brackets too) ?
# u might wanna find a special function in python

    try:
        
        expression = input("Enter arithmetic expression: ")
        result = eval(expression) 
        print(f"Output: {result}")
    except Exception as error:
        print(f"Exception: {error}")
    finally:
        choice = input("Do you want to continue? [y/n] : ")

