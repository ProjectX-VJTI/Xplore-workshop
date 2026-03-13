choice = 'y'

while choice =='y'or choice == 'Y': # make 'Y' valid too
    try:
        # typecast the below 2 to a list
        
        numbers = list(map(int,input("Enter the input numbers separated by spaces: ").split()) )
        operators =  input("Enter operators between them: ").split()

        # check length matching

        if len(numbers) != len(operators) + 1 : # this seems odd... u might say it's ... off by one
             print("The number of operators are less than numbers by one") # replace wiht better message :)
             continue
        
        flag = False # huh this seems inverted
        for i in range(len(operators)) : # indexing range fix
            a,b,op = numbers[i],numbers[i+1],operators[i]
            # correct the ops
            match op:
                case '+':
                    c = a+b
                case '-':
                    c = a-b
                case '*':
                    c = a*b
                case '/':
                    c = a/b
                case '%':
                    c = a%b
                case '//':
                    c = a//b
                case '**':
                    c = a**b
                case _:
                    flag = True
            if  flag:
                print("Invalid ops vro")
                break

            numbers[i+1] = c
        if not flag :
         print(f"Output:  {numbers[-1]}")
    except Exception as e :
        print(f"Exception:  {e}") # print exception
    finally:
        choice = input("Do you want to continue? [y/n] : ") # always ask before ending

# can you make the code shorter and with improved answer? 
# like handling any basic arithmetic equation (that may have brackets too) ?
# u might wanna find a special function in python