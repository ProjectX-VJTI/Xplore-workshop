# Strings: Data type that stores a sequence of characters
a="hello"
b="world"
print(a+b) # Concatenation
str="Monkey D. Luffy"
str2='Roronoa Zoro' # Can use both single and double quotes
print(len(str))
print("Straw Hat Pirates\nOne Piece\tEichiro Oda") # Escape Sequence
str3=str+str2
print(str3)
print(len(str3))

# Indexing: From 0 index, It helps in accessing characters
str="Harsh Sankhe"
print(str[0],str[6]) # We cannot modify values with indexing
"""
str="Harsh Sankhe"
str[0]='P'
print(str)
This will give us an error
"""

# Slicing: Accessing parts of string
## Str[starting_idx : ending_idx] ending_idx is not included
str="Monkey D. Garp"
print(str[1:9])
print(str[:9])
print(str[:len(str)])
print(str[7:])

# Negative Index: Last Idx is -1
str="Apple"
print(str[-3:-1])

# String Functions
str="i Am a good coder"

## str.endswith() function
print(str.endswith("er")) # returns true if string ends with substr

## str.capitalize() function
print(str.capitalize()) # capitalize only 1st char and make others lower case
str1=str.capitalize()
print(str)
print(str1)

## str.find(word) function
print(str.find("coder")) # returns 1st index of 1st occurence

## str.count("am") function
print(str.count("Am")) # counts the occurence of substr in string

## str.replace(old,new) function
print(str.replace("Am","Are")) # replaces all occurences of old with new
str2=str.replace("o","a")
print(str2)

# WAP to input user's first name & print its length
firstName=input("Enter first name: ")
lengthName=len(firstName)
print(lengthName)

# WAP to find occurence of '$' in a given string
str=input("Enter the string")
count=str.count("$")
print(count) 
