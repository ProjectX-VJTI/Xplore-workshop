choice = 'y'

while choice.lower() =='y':
    try:
        # typecast the below 2 to a list
        
        numbers =[float(x) for x in input("Enter the input numbers separated by spaces: ").split()]
        print(type(numbers))
        operators =input("Enter operators between them: ").split()
        print(type(operators))

        if len(numbers) !=               len(operators) + 1:
            print("Length of operators is not matching") #better?
            continue
        
        flag = False 
        
        for i in range(1, len(numbers)):
            a, b, op = numbers[i-1], numbers[i], operators[i-1]
            
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
                    print("Invalid operator")
                    flag = True
                    break

            numbers[i] = c
        
        if flag:
            continue
        print(f"Output: {numbers[-1]}")
        
    except Exception as e:
        print(f"Exception: {e} ") 
        
    finally:
        choice = input("Do you want to continue? [y/n] : ")

# can you make the code shorter and with improved answer? 
# like handling any basic arithmetic equation (that may have brackets too) ?
# u might wanna find a special function in python

#shortened code 
choice = 'y'

while choice.lower() == 'y':
    try:
        expression = input("Enter an arithmetic expression: ")
        result = eval(expression)  
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        choice = input("Do you want to continue? [y/n]: ")