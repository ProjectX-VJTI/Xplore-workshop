choice = 'y'

## FIX : using 'or' to add 'Y' case also

while (choice =='y' or choice == 'Y'): # make 'Y' valid too
    try:
        # typecast the below 2 to a list

        # FIX: Added 'float' to map and split the input correctly
        numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
        # FIX: Just split the string to get a list of operator strings
        operators = input("Enter operators between them: ").split()
        # operators = input("Enter operators between them: ")
        
        
        # check length matching

        # FIX: numbers should be exactly 1 more than operators
        if len(numbers) != 1 + len(operators): 
            print("Error: Provide n numbers and n-1 operators!")
            continue
        ## FIX : Set flag to True
        flag = True
        for i in range(1, len(numbers)):
            a, b, op = numbers[i-1], numbers[i], operators[i-1]
            
            ## FIX : Correcting the mismatched operators
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
                    break
            ## FIX
            numbers[i] = c
        
        ## FIX
        if not flag:
            print("Invalid ops vro")
        else:
            print(f"Output: {numbers[-1]}")
            
    except Exception as e:
        print(f"Exception: {e}") 
    finally:
        choice = input("Do you want to continue? [y/n] : ")

# can you make the code shorter and with improved answer? 
# like handling any basic arithmetic equation (that may have brackets too) ?
# u might wanna find a special function in python