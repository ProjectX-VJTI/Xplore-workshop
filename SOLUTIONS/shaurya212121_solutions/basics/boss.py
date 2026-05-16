choice = 'y'

while choice =='y'or choice=='Y': # make 'Y' valid too
    try:
        # typecast the below 2 to a list
        equation = input("Enter the full equation (e.g. 2 + 3 * (4 / 2)): ")
        
        # check length matching

        if not any(char.isdigit() for char in equation): # this seems odd... u might say it's ... off by one
            print("Please enter a valid mathematical expression.") # replace wiht better message :)
            continue
        
        flag = True # huh this seems inverted
        # indexing range fix
        # correct the ops
        
        # eval() handles brackets, precedence, and all basic operators automatically
        result = eval(equation)

        if not flag:
            print("Invalid ops vro")
            break

        if flag:
            print(f"Output: {result}")
    except Exception as e:
        print(f"exception: {e}") # print exception
    finally:
        choice = input("Do you want to continue? [y/n] : ") # always ask before ending