choice = 'y'

while (choice =='y'|choice=='Y') : # make 'Y' valid too
    try:
        # typecast the below 2 to a list
        
        numbers =list(input("Enter the input numbers separated by spaces: "))
        operators =list( input("Enter operators between them: "))

        # check length matching

        if len(numbers) != len(operators) + 1: # missed error : (
            print("length is not equal ") # replace wiht better message :)
            continue
        
        flag = True # huh this seems inverted
        for i in range(0,len(operators)): # indexing range fix
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

            numbers[i+1] = c # fix index
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