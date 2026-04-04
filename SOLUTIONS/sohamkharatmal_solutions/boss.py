choice = 'y'

while choice =='y' or choice =='Y': # make 'Y' valid too
    try:
        # typecast the below 2 to a list
        numbers = list(map(int, input("Enter numbers: ").split()))
        operators = input("Enter operators between them: ").split()

        # check length matching

        if len(numbers)-1 != len(operators): # this seems odd... u might say it's ... off by one,now condition updated
            print("Number of operator should be one less than number of operands") # replace wiht better message :) "very formal reply"
            continue
        
        flag = True # huh this seems inverted, but corrected now
        for i in range(1,len(numbers)): # indexing range fix, added start and stop condition
            a, b, op = numbers[i-1], numbers[i], operators[i-1]
            # the ops are revised
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
                print("Invalid operator entered")
                break

            numbers[i] = c
        if not flag:
            continue
        print(f"Output: {numbers[-1]}")
    except Exception as e:
        print(f"Exception: {e}") # print exception
    finally:
        choice = input("Do you want to continue? [y/n] : ") # always ask before ending

# can you make the code shorter and with improved answer? 
# like handling any basic arithmetic equation (that may have brackets too) ?
# u might wanna find a special function in python