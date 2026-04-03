choice = 'y'

while (choice =='y' or choice=='Y') : # make 'Y' valid too
    try:
        # typecast the below 2 to a list
        
        numbers =input("Enter the input numbers separated by spaces: ").split()
        operators = input("Enter operators between them: ").split()

        # check length matching

        if (len(numbers)-1) != len(operators): # this seems odd... u might say it's ... off by one
            print("try again!") # replace wiht better message :)
            continue
        
        flag = True # huh this seems inverted
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
                print("Invalid ops vro")
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

#improved code logic:
choice2='y'
while(choice2=='y'or choice2=='Y'):
    expression=input("Enter the expression")
    try:
        result=eval(expression)
        print(result)
    except Exception:
        print("invalid!")
    finally:
        choice2=input("do you want to continue?")





