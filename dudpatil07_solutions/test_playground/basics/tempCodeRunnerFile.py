choice = 'y'

while choice.lower() =='y' : # make 'Y' valid too
    try:
        # typecast the below 2 to a list
        
        numbers = list(map(int, input("Enter the input numbers separated by spaces: ").split()))
        operators = input("Enter operators between them: ").split()

        # check length matching

        if len(operators) != len(numbers)-1: # this seems odd... u might say it's ... off by one
            print("Number of operators must be one less than numbers ") # replace wiht better message :)
            continue
        
        flag = False # huh this seems inverted
        for i in range(1,len(numbers)): # indexing range fix
            a, b, op = numbers[i-1], numbers[i], operators[i-1]
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
                case _:
                    flag = true
