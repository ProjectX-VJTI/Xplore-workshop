# Lists: A built in data type that stores set of values

marks=[94.4,56,78,66.4,55]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))
## It can store elements of different types
student=["Karan",85,"Delhi"]
student[0]="Arjun"
print(student)
"""
Strings are immutable whereas Lists are mutable
That means we can access values in string but can't change it
but in lists we can both access and change the values

Also here lists print(marks[9]) will give error as we are going out of bound
"""

# List Slicing: Similar to string slicing
## list_name[starting_idx : ending_idx] ending idx is excluded
marks=[87,64,33,95,76]
print(marks[1:4])
print(marks[:4])
print(marks[1:])
print(marks[-3:-1])

# List Methods(Functions)
list=[2,1,3]

## list.append adds one element at the end
list.append(4)
print(list)

## list.sort in ascending order
list.sort()
print(list)

## list.sort(reverse=True)
list.sort(reverse=True)
print(list)

## list.reverse() reverses list
list.reverse()
print(list)

## list.insert(idx,ele) insert element at index
list.insert(1,5)
print(list)
list.insert(1,2)
list.insert(1,1)
list.insert(6,5)
print(list)

## list.remove(1) removes first occurence of element
list.remove(5)
print(list)

## list.pop(idx) removes element at idx
list.pop(3)
print(list)

# Tuples: A built in data type that lets us create immutable sequence of values

tup=(87,64,33,95,76)
print(tup)
print(type(tup))
# tup[0]=5 is not allowed here will give an error
tup=(1,)
tup2=(1) # Will give int datatype as no comma
tup3=()
print(type(tup))
print(type(tup2))
print(type(tup3))

# Tuple Slicing: Very Similar to list and string slicing
tup=(1,2,3,4)
print(tup[1:3])

# Tuple Methods
tup=(2,1,3,1)

 ## tup.index(el) returns index of first occurence
print(tup.index(1))

## tup.count(el) counts total occurrences tup.count(1) is 2
print(tup.count(1))

# WAP to ask the user to enter names of their fav 3 movies and store them in list
movie=[]
movie.append(input("Enter first fav movie: "))
movie.append(input("Enter second fav movie: "))
movie.append(input("Enter third fav movie: "))
print(movie)

# WAP to check if a list contains a palindrome of elements
# Hint use copy() method
list=[1,2,3,4,1]
list2=list.copy()
list2.reverse()
if(list==list2):
    print("PALINDROME")
else:
    print("NOT A PALINDROME")

# WAP to count the number of students with "A" grade in the following tuple
tup=("C","D","A","A","B","B","A")
print(tup.count("A"))

# WAP to store "C","D","A","A","B","B","A" in a list and sort them from A to D
list=["C","D","A","A","B","B","A"]
list.sort()
print(list)
