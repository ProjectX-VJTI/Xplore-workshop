# Loops: Loops are used to repeat instructions

# while Loops
# while condition:
#   some work

count=1 # Here count is an iterator
while count<=5:
    print("Hello")
    count+=1
print(count) # Will give 6 as count is increasing by one

i=1000
while i>=1:
    print(i,"Harsh Sankhe")
    i-=1
print("Loop Ended")

# Try to avoid infinite loop in any condition

# Print numbers from 1 to 100
i=1
while i<=100:
    print(i)
    i+=1

# Print numbers from 100 to 1
i=100
while i>=1:
    print(i)
    i-=1

# Print multiplication table of number n
n = int(input("Enter any number: "))
p = 1
while p <= 10:
    print(n * p)
    p += 1


# Print elements of following list using a loop
list=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(list):
    print(list[i])
    i+=1

# Search for a number x in this tuple using a loop
tup=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter a number x: "))
i=0
found=None
while i<len(tup):
    if(tup[i]==x):
        found=True
        break
    else:
        found=False
    i+=1
if(found):
    print("Element found at",i)
else:
    print("Not Found")

# Break & Continue
# Break: Used to terminate the loop when encounterd
# Continue: Terminates the execution in the current iteration & continue execution of loop with next iteration
# Break
i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1
print("Loop ended")
# Continue
i=1
while i<=5:
    if(i==3):
        i+=1
        continue  # Act as skip
    print(i)
    i+=1

# Print odd numbers from 1 to 100
i=1
while i<=100:
    if(i%2==0):
        i+=1
        continue  # Act as skip
    print(i)
    i+=1

# for Loops: Loops are used for sequential traversal for traversing list, string tuples etc

# for Loops 
# for el in list
#   some work
num=[1,2,3,4,5]
veggies=("potato","tomato","brinjal","ladyfinger")
name="Harsh Sankhe"

for val in num:
    print(val)

for val in veggies:
    print(val)

for val in name:
    print(val)

# for Loops with else
# for el in list:
#   some work
# else:
#   work when loop ends

for val in name:
    if(val=='o'):
        print("o found")
        break
    print(val)
else:
    print("END") # else wala kaam will not be executed in break condition

# Print elements of following list using a loop
list=[1,4,9,16,25,36,49,64,81,100]

for el in list:
    print(el)

# Search for a number x in this tuple using a loop
tup=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter a number x: "))
idx=0
for el in tup:
    if(el==x):
        print("Element found at idx",idx)
        break
    idx+=1

# range() function
# Range function returns a sequence of numbers, starting from 0 by default, and increments by 1(by default) ad stops before a specified number
# range(start?,stop,step?)

seq=range(10)
for i in seq:
    print(i)

for el in range(5): # range(stop)
    print(el)

for el in range(2,10): # range(start,stop)
    print(el)

for el in range(2,10,2): # range(start,stop,step)
    print(el)

# Using for & range()

# Print numbers from 1 to 100
for i in range(1,101):
    print(i)

# Print numbers from 100 to 1
for i in range(100,0,-1):
    print(i)

# Print the multiplication table of number n
n=int(input("Enter a value of number: "))
for i in range(n,11*n,n):
    print(i)

# pass Statement
# pass is a null statement that does nothing.It is used as a placeholder for future code
for el in range(10):
    pass

print("With help of pass we can escape indentation error")

# WAP to find the sum of first n natural numbers. (using while)
n=int(input("Enter number for sum: "))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1
print(sum)

# WAP to find factorial of a number n. (using for)
n=int(input("Enter number to find factorial: "))
fact=1
for i in range(1,n+1):
    fact*=i
print("Factorial=",fact)
