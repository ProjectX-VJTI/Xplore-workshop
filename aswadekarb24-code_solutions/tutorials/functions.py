# Functions: Block of statements that perform specific tasks
# def func_name(para1, para2,...):
#    some work
#    return value

# func_name(arg1,arg2,...) function call

def calc_sum(a,b):
    sum=a+b
    return sum

print(calc_sum(5,12)) # Helps in reducing redudancy
print(calc_sum(9,44))
sum=calc_sum(6,89)
print(sum)

def print_hello():
    print("Hello")
    return

print_hello()
output=print_hello() # None function
print(output)

# Avg of 3 numbers
def avgOf3 (a,b,c):
    avg=(a+b+c)/3
    return avg

print(avgOf3(9,8,7))

# Types of function: Built In functions and User Defined functions

# Default Parameters: Assigning a default value to parameter, which is used when no argument is passed

def call_prod(a,b):
    return a*b

# print(call_prod()) will give an error as no argument is passed

def call_prod(a=2,b=1):
    return a*b

print(call_prod())  # Will not give error even with no arg as it will take 2,1 as default

def call_prod(a,b=1):
    return a*b

# def call_prod(a=2,b):   this will give error as only non-default parameter can follow default parameter
#     return a*b

# That's why we give default values from last

# WAP to print length of list.(list is the parameter)
def lenOfList(list):
    length=len(list)
    print(length)
    return length

list1=[1,4,9,16,25,36,49]
list2=[]
lenOfList(list1)
lenOfList(list2)

# WAP to print the elements of a list in a single line. (list is the parameter)
def printList(list):
    print(list)
    return 

list1=[1,4,9,16,25,36,49]
printList(list1)

# WAP to find the factorial of n. (n is the parameter)
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

print(factorial(6))

# WAP to convert USD to INR
def currConv(USD):
    INR=USD*83
    return INR

print(currConv(5))

# WAP to tell whether a number is odd or even
def oddEven(num):
    if(num%2==0):
        print("EVEN")
    else:
        print("ODD")
    
oddEven(98)
oddEven(-3)
oddEven(0)

# Recursion: When a function calls itself repeatedly
# Print n number backwards
def show(n):
    if(n==0):  # Base Call
        return
    print(n)
    show(n-1)   # Recursive Call

show(6)

# Return n!
def factorial(n):   
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1) # Recurrence relation

print(factorial(10))

# Write a recursive function to calculate the sum of first n natural numbers
def sumRecursion(n):
    if(n==1):
        return 1
    return n+sumRecursion(n-1)

print(sumRecursion(10))

# Write a recursive function to print all elements in a list
# Hint: Use list & index as parameters
def printList(list,index):
    if(index==len(list)):
        return
    print(list[index])
    return printList(list,index+1)

list1=[1,4,9,16,25,36,49]
printList(list1,0)
