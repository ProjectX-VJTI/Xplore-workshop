choice = 'y'

while (choice =='y' or choice == 'Y') :
    try:
        numbers = input("Enter the input numbers separated by spaces: ").split(" ")
        operators = input("Enter operators between them: ").split(" ")

        if len(numbers)-1 != len(operators): # this seems odd... u might say it's ... off by one
            print("The number of operators should be one less than the number of operands") # replace wiht better message :)
            continue
        
        flag = True # huh this seems inverted
        c=0
        for i in range(1,len(numbers)): # indexing range fix
            a, b, op = int(numbers[i-1]), int(numbers[i]), operators[i-1]
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
                print("Invalid operators")
                break

            numbers[i] = str(c)
        if not flag:
            continue
        print(f"Output:", numbers[-1])
    except Exception:
        print(f"Invalid Input, try again") # print exception
    finally:
        choice = input("Do you want to continue? [y/n] : ") # always ask before ending

# can you make the code shorter and with improved answer? 
# like handling any basic arithmetic equation (that may have brackets too) ?
# u might wanna find a special function in python