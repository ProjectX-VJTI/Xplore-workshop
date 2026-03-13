# typecast all inputs as prompted

# note: all inputs are strs by default


integer = int(input("Enter an integer: "))  # change only this line

print(type(integer)) # should output 'int'

number = float(input("Enter a number (floating point allowed): ")) # change only this line

print(type(number)) # should output 'float'

array = list(input("Enter an array of numbers: ").split()) # change only this line

print(type(array)) # should output 'list'

nums = ','.join(map(str, [1,2,3,4]))

print(nums) # print it as a string joined by commas : 1,2,3,4


name = input("Enter your name: ")

print(f"Hello, {name}") # complete f string

x,y,z = 67, 420 , 9000


# 6 print statements is too much, can you get the same output in one print statement ?
print(x,'\n',y,'\n',z,sep=" ")