# Dictionary: Used to store data values in key:value pairs
# They are unordered, mutable & don't allow duplicate keys
# dict["key"]="value"
dict={
    "key":"value",
    "name":"Harsh Sankhe",
    "learning":"Python",
    "age":19,
    "is_adult":True,
    "marks":99.99,
    12:100,
    "list":["C","C++","Python"],
    "tup":("dict","set")
}
print(dict)
print(type(dict))
print(dict["name"])
print(dict[12])
print(dict["list"])
dict["name"]="Luffy"  # Overwrite
dict["new_key"]="ZORO" # Will be added at end as new key:value pair
print(dict)
null_dict={}
print(null_dict)
null_dict["key1"]="value1"
null_dict["key2"]=2
null_dict["key3"]=True
print(null_dict)

# Nested Dictionaries
student={
    "name":"Harsh Sankhe",
    "subjects":{
        "phy":92,
        "maths":95,
        "chem":97,
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["chem"])

# Dictionary Methods

myDict={
    "name":"Harsh Sankhe",
    "subjects":{
        "phy":92,
        "maths":95,
        "chem":97,
    }
}

## myDict.keys() returns all keys
print(myDict.keys())
print(list(myDict.keys()))
print(len(list(myDict.keys())))

## myDict.values() returns all values
print(myDict.values())
print(list(myDict.values()))

## myDict.items() returns all (key,val) pairs as tuples
print(myDict.items())
print(list(myDict.items()))
pairs=list(myDict.items())
print(pairs[0])

## myDict.get("key") returns all keys according to values
print(student["name"])
print(student.get("name")) # This is more efficent to use
# print(student["name2"]) it will cause error as name2 is not there
print(student.get("name2")) # Will not give any error

## myDict.update(newDict) inserts the specified item to dictionary
new_dict={
    "city":"mumbai",
    "age":18,
    "name":"LUFFY"
}
myDict.update(new_dict)
print(myDict)

# Set: Set is the collection of unordered items
# Each element in the set must be unique and immutable
nums={1,2,3,4,"hello",8.9}
set2={1,2,2,2}
print(nums)
print(set2) # repeated element stored only once so it resolved to {1,2}
null_set=set()
emptySet=set()
print(null_set)
# List and Dictionary cannot be stored in set as they are mutable
print(nums)
print(len(nums))
# Also note that Sets are multable but elements of sets are immutable

# Set Methods

collection=set()

## set.add(ele) adds element in set
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(2)
collection.add((1,2,3))
# collection.add([1,2,3]) will give an error as list cannot be added
print(collection)

## set.remove(ele) removes element in a set
collection.remove(3)
print(collection)

## set.pop() removes a random value
collection.pop()
print(collection)

## set.clear() empties the set
collection.clear()
print(collection)

## set.union(set2) combines both set & return new
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(set1.union(set2))

## set.intersection() combines common value & returns new
print(set1.intersection(set2))

# WAP to store the following word meaning in python dictionary
ans={
    "table":["a piece of furniture", "list of facts & figures"],
    "cat":"a small animal"
}
print(ans)

# You are given a list of subjects for students assume one classroom
# for 1 subject. How many classrooms for all students.
list1=["python","java","C++","python","javascript","java","python","java","C++","C"]
NoOfClass=len(set(list1))
print(NoOfClass)

# WAP to enter marks of 3 subjest from user and store them in a dictionary
# Start with an empty dictionary & add one by one. Use subject name as key & marks as value
marks={}
x=int(input("Enter phy marks: "))
marks.update({"Phy":x})

y=int(input("Enter chem marks: "))
marks.update({"Chem":y})

z=int(input("Enter maths marks: "))
marks.update({"Maths":z})
print(marks)

# Figure out a way to store 9 and 9.0 as seprate values in the set
value1=9
value2=float(value1)
values={value1,value2}
print(values)
