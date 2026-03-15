choice = 'y'

while (choice =='y' or choice == 'Y') :
    try:
       exp = input("Enter the expression to be evaluated: ")
       print("Output:", eval(exp))
    except Exception:
        print(f"Invalid Input, try again") # print exception
    finally:
        choice = input("Do you want to continue? [y/n] : ") # always ask before ending

# can you make the code shorter and with improved answer? 
# like handling any basic arithmetic equation (that may have brackets too) ?
# u might wanna find a special function in python