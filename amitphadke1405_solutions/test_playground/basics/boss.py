choice = 'y'
#this code displays result of executing expression from left to right
while (choice =='y' or choice=='Y') : # make 'Y' valid too
    try:
        # typecast the below 2 to a list
        
        numbers =list(map(int,input("Enter the input numbers separated by spaces: ").split()))
        operators = input("Enter operators between them: ").split()

        # check length matching

        if len(numbers) != len(operators)+1: # this seems odd... u might say it's ... off by one
            print("What u doin fam ? ") # replace wiht better message :)
            continue
        
        flag = True # huh this seems inverted
        c=numbers[0]
        for i in range(1,len(numbers)): # indexing range fix
            a, b, op = c, numbers[i], operators[i-1]
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

            #numbers[i] = c
        if not flag:
            continue
        print(f"Output: {c}")
    except Exception as error:
        print(f"Exception: {error}") # print exception
    finally:
        choice = input("Do you want to continue? [y/n] : ") # always ask before ending

# can you make the code shorter and with improved answer? 
# like handling any basic arithmetic equation (that may have brackets too) ?
# u might wanna find a special function in python