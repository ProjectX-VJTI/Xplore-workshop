choice = 'y'

# Handling 'y' and 'Y' for the loop
while choice.lower() == 'y':
    try:
        # Instead of separate lists for numbers and ops, 
        # we just take the whole math string!
        equation = input("Enter your math equation (e.g., (10 + 5) * 2): ")

        # eval() takes the string and solves it according to BODMAS/PEMDAS
        result = eval(equation)
        
        print(f"Output: {result}")

    except ZeroDivisionError:
        print("Error: Lil bro, you can't divide by zero!")
    except Exception as e:
        # This catches syntax errors like "5 ++ 5"
        print(f"Exception: {e}. Check your math syntax!")
    
    finally:
        # This ensures we always ask to continue even if there was an error
        choice = input("Do you want to continue? [y/n] : ")

# can you make the code shorter and with improved answer? 
# like handling any basic arithmetic equation (that may have brackets too) ?
# u might wanna find a special function in python