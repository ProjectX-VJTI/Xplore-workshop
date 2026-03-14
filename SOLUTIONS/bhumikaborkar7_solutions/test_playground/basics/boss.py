choice = 'y'

while choice =='y' or choice=='Y': # make 'Y' valid too
    try:
        # typecast the below 2 to a list
        
        numbers =list(map(int, input("Enter the input numbers separated by spaces: ").split()))
        operators = input("Enter operators between them: ")

        # check length matching

        if len(operators) != len(numbers)-1: # this seems odd... u might say it's ... off by one
            print("Number of operators is not correct!") # replace with better message :)
            continue
        
        flag = False # huh this seems inverted
        for i in range(len(operators)): # indexing range fix
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
                    flag = True
            if flag:
                print("Invalid ops vro")
                break

            numbers[i+1] = c
        if not flag:
            print(f"Output: ", {numbers[-1]})
    except Exception as e:
        print("Exception: ...", e) # print exception
    finally:
        choice = input("Do you want to continue? [y/n] : ") # always ask before ending

# can you make the code shorter and with improved answer? 
# like handling any basic arithmetic equation (that may have brackets too) ?
# u might wanna find a special function in python

#trying shorter version

choice='y'
while choice=='Y' or choice=='y' :
    try:
        ex=input("Enter an expression: ")
        print("output:",eval(ex))
    except Exception as e:
        print("Error:", e)
    finally:
        choice= input("Press Y to continue: ")