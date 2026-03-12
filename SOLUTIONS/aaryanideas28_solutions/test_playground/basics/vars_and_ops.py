# declare some variables

x = 10
y = 5
## CHANGE : Deleted this line -> y = "5"

print(x+y) # come on think, this ain't javascript

## CHANGE : y is an integer not a string so y = 5 and not y = "5"

num1 , num2 = 6 , 7

# print(num1 // num2 .:2f) # huh this shouldnt output 0, as a bonus can u also round to 2 decimal places?

## FIX: used f string and .2f for 2 decimal places: 
print(f"{num1 / num2 :.2f} ")


a , n = 1, 31

# for i in range(n):
#     a *= 2 # can you replace this loop with a one liner?

print(a**n) 

# match the correct statements wrt bitwise operators

print("AND operator:", " & ")
print("OR operator:", " | ")
print("XOR operator:", " ^ ")



