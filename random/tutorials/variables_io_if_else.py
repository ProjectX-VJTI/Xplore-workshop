# First Program
print("Hello World!","Printing on same line.")
print("Harsh is my name and I am",18,"years old.")
print(26)
print(15+16)

# Variables: Name given to a memory location 
name="Harsh" 
age=18
price=99.99
print("Name:",name)
print("Age:",age)
print("Price:",price)
age2=age
print("My name is",name,"and I am",age2,"years old.") 

# Types of variables
print(type(name))
print(type(age))
print(type(price))
old=False
a=None
print(type(a))
print(type(old))

# Print Sum
x=5000
y=400
sum=x+y
diff=x-y
print(sum)
print(diff)

# Types of operators
# Arithmetic (+,-,*,/,%,**)
# Relational (==,>=,<=,!=,>,<)
# Assignment (+=,-=,/=,*=,%=,**=)
# Logical    (not,and,or)
print(20==50)

# Exponent
a=2
b=5
c=a**b
print(c)

# Logical operator: and,not,or Operator precedence: not>and>or

# Type conversion
a,b=1,2.0
sum=a+b
print(sum)
"""
ERROR:
a,b=1,"2.0"
sum=a+b
"""

# Type casting
a,b=1,"2"
c=int(b)
sum=a+c
print(sum)

a=3.14
a=str(a)
print(type(a))

# Expression Execution: 

## String & Numeric values can operate together with *
a,b=2,3
txt="@"
print(a*b*txt)

## String & String can operate together with + (Concatenation)
p,q="$",3
print((p+txt)*q)

## Numeric values can operate with all arithmetic operators
A,B=2,4
C=6
print((B+C)*A)

## Arithmetic expression with integer and float will result in float
A,B=10,5.0
C=A*B
print(C)

## Result of divison operator with two integers will be float
A,B=1,2
print(A/B)

## Integer division with float and int will give int displayed as float
A,B=1.5,3
C=A//B
print(C,A/B)

## Floor gives closest integer, which is lesser than or equal to the float value
## Result of (A//B) is same as floor(A/B)
X,Y=12,5
Z=X//Y
print(Z)

X,Y=-12,5
Z=X//Y
print(Z)

X,Y=12,-5
Z=X//Y
print(Z)

## Remainder is only negative when denominator is negative
A,B=-5,2
C=A%B
print(C)

A,B=5,-2
C=A%B
print(C) 

# Comments
#print("Hello World!")
"""This is
a multi line
comment"""

# Inputs in python
name=input("Name: ")
age=int(input("Age: "))
price=float(input("Price: "))
print("You are",name,"who is",age,"years old and has value",price)

# Conditional statements
# if-elif-else sentax with indentation(4 spaces)
age=int(input("Enter your age: "))
if(age>=18):
    print("You can vote")
elif(age<18):
    print("You cannot vote")
else:
    print("Enter a valid age")

# Traffic light code
light=input("Enter light: ")
if(light=="red"):
    print("STOP")
elif(light=="yellow"):
    print("LOOK")
elif(light=="green"):
    print("GO")
else:
    print("BROKEN")

# Grades of students
marks=int(input("Enter your marks: "))
if(marks>=90):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
elif(marks>=70 and marks<80):
    print("C")
else:
    print("D")

# Ternary operator
food=input("Food: ")
eat="YES" if(food=="cake") else "NO"
print(eat)

food=input("Food: ")
print("SWEET") if(food=="cake" or food=="jalebi") else print("NOT SWEET")

# Clever If ternary operator
age=int(input("Age: "))
vote=("NO","YES") [age>=18]

sal=float(input("Salary :"))
tax=sal*(0.1,0.2) [sal>50000]
print(tax)

# WAP to check if a number entered by user is odd or even
num=int(input("Enter a number: "))
if(num%2==0):
    print("Even Number")
else:
    print("Odd Number")

# WAP to find the greatest of 3 numbers entered by user
p=int(input("Enter first number: "))
q=int(input("Enter second number: "))
r=int(input("Enter third number: "))
if(p>=q and p>=r):
    print(p,"is largest number")
elif(q>=p and q>=r):
    print(q,"is largest number")
else:
    print(r,"is largest number")

# WAP to check if a number is a multiple of 7 or not
num=int(input("Enter a number: "))
if(num%7==0):
    print("Multiple of 7")
else:
    print("Not a multiple of 7")
    