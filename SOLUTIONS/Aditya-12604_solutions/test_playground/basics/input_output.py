# typecast all inputs as prompted

# note: all inputs are strs by default


integer = input("Enter an integer: ") # change only this line

print(type(integer)) # should output 'int'

number = input("Enter a number (floating point allowed): ") # change only this line

print(type(number)) # should output 'float'

array = input("Enter an array of numbers: ") # change only this line

print(type(array)) # should output 'list'

nums = [1,2,3,4]

print(nums) # print it as a string joined by commas : 1,2,3,4


name = input("Enter your name: ")

print(f"Hello, name") # complete f string

x,y,z = 67, 420 , 9000


# 6 print statements is too much, can you get the same output in one print statement ?
print(x)
print('\n')
print(y)
print('\n')
print(z)

