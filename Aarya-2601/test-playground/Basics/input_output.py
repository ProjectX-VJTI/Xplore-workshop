integer = int(input("Enter an integer: "))
print(type(integer))
#typecasting is done by specifying type(input(statement))

number = float(input("Enter a number (floating point allowed): "))
print(type(number)) 

array = [float(x) for x in input("Enter an array of numbers: ").split()]
print(type(array))
 #In Python, the split() function is a built-in string method used to break a single string into a list of substrings based on a specified delimiter. It is widely used for data cleaning, text parsing (like reading CSV rows), and processing user input. 

nums = [1,2,3,4]
print(",".join(map(str, nums)))
#map(): This function iterates over an entire array or iterable and applies a specific transformation function to each individual element, creating a new array with the results. It is used to process the data elements one by one.
#join(): This method is then called on the new array created by map() to concatenate all of its elements into a single string, using an optional separator you specify (e.g., a comma and space, an empty string, etc.)

name = input("Enter your name: ")
print(f"Hello, {name}")
#variable name must be enclosed in {} and prefixed with f to indicate that it is a formatted string literal

x,y,z = 67, 420 , 9000
print(x,'\n',y,'\n',z)
