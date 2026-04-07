# typecast all inputs as prompted

# note: all inputs are strs by default

# 1. Typecasting to Integer
integer = int(input("Enter an integer: ")) 
print(type(integer))

# 2. Typecasting to Float
number = float(input("Enter a number (floating point allowed): ")) 
print(type(number)) 

# 3. Typecasting to List
# .split() takes a string like "1 2 3" and makes it ["1", "2", "3"]
array = input("Enter an array of numbers (separated by spaces): ").split()
print(type(array)) 

# 4. Printing list as a string joined by commas
nums = [1, 2, 3, 4]
# map(str, nums) converts each number to a string so .join can work
print(",".join(map(str, nums))) 

# 5. Completing the f-string
name = input("Enter your name: ")
print(f"Hello, {name}") 

# 6. One print statement challenge
x, y, z = 67, 420, 9000

# sep="\n\n" puts two newlines between each variable
print(x, y, z, sep="\n\n")

