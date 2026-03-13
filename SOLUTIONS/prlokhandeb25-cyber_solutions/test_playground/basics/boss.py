choice = 'y'

while choice.lower() =='y' : # make 'Y' valid too
    try:
        expr=input("Enter arithmetic Expression: ")
        result=eval(expr)
        print("output: ",result)
        
        #numbers =list(map(int,input("Enter the input numbers separated by spaces: ").split()))
        #operators = input("Enter operators between them: ").split()
        #if len(operators) != len(numbers)-1: 
            #print("INVALID EXPR ") 
            #continue
        #flag = True 
        #result=numbers[0]
        #for i in range(len(operators)): 
            #a, b, op = result, numbers[i+1], operators[i]
            # correct the ops
            #if op == '+':
               #result = a + b
            #elif op == '-':
                #result = a - b
            #elif op == '*':
                #result = a * b
            #elif op == '/':
                #result = a / b
            #elif op == '%':
                #result = a % b
            #elif op == '//':
                #result = a // b
            #elif op == '**':
                #result = a ** b
            #else:
                #flag = False
                #print("Invalid operator detected!")
                #break
        #if flag:
            #print(f"Output: {result}")
    except Exception as e :
        print(f"Exception:{e}") # print exception
    finally:
        choice = input("Do you want to continue? [y/n] : ") # always ask before ending

# can you make the code shorter and with improved answer? 
# like handling any basic arithmetic equation (that may have brackets too) ?
# u might wanna find a special function in python