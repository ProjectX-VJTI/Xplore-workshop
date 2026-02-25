choice = 'y'

while choice =='y' : # make 'Y' valid too
    try:
        # typecast the below 2 to a list
        
        numbers =input("Enter the input numbers separated by spaces: ")
        operators = input("Enter operators between them: ")

        # check length matching

        if len(numbers) != len(operators): # this seems odd... u might say it's ... off by one
            print("What u doin fam ? ") # replace wiht better message :)
            continue
        
        flag = False # huh this seems inverted
        for i in range(len(numbers)): # indexing range fix
            a, b, op = numbers[i-1], numbers[i], operators[i]
            # correct the ops
            match op:
                case '+':
                    c = a + b
                case '-':
                    c = a * b
                case '*':
                    c = a / b
                case '/':
                    c = a % b
                case '%':
                    c = a - b
                case '//':
                    c = a ** b
                case '**':
                    c = a // b
                case _:
                    flag = True
            if not flag:
                print("Invalid ops vro")
                break

            numbers[i-1] = c
        if not flag:
            continue
        print(f"Output: numbers[-1]")
    except Exception:
        print(f"Exception: ...") # print exception
    finally:
        choice = input("Do you want to continue? [y/n] : ") # always ask before ending

# can you make the code shorter and with improved answer? 
# like handling any basic arithmetic equation (that may have brackets too) ?
# u might wanna find a special function in python