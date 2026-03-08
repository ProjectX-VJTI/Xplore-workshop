# File I/O: Python can be used to perform operations on a file.(read & write data)
# Types of all files
# 1. Text Files: .txt, .docx, .log etc
# 2. Binary Files: .mp4, .mov, .png, .jpeg etc

# Open, read & close file
# We have to open a file before reading or writing
# f=open("file_name","mode")     Here file name can be sample.txt or demo.docx and the mode can be r:read mode or w:write mode (default mode is r)
# data=f.read()
# f.close()

f=open("Python/Sample.txt","r")
data=f.read()
print(data)
print(type(data))
f.close()

"""
Character   |   Meaning
    'r'     |   open for reading(default)
    'w'     |   open for writing, truncating the fle first(overwriting)
    'x'     |   create a new file and open it for writing
    'a'     |   open for writing, appending to end of list if exists
    'b'     |   binary mode
    't'     |   text mode(defaults)
    '+'     |   open a disk file for updating(reading and writing)
"""

# Reading a file
# data=f.read()     reads entire file 
# data=f.readline() reads one line at a time
f=open("Python/Sample.txt","r")
data=f.read(17)     # Gives character till that specific character
print(data)
f.close()

f=open("Python/Sample.txt","r")
line1=f.readline()
line2=f.readline()
print(line1)
print(line2)
f.close()

# Writing to a file
# f=open("Sample.txt","w")
# f.write("This is a new line")   overwrites the entire file

# f=open("Sample.txt","a")
# f.write("This is a new line")   adds to the file

f=open("Python/Sample.txt","w")
f.write("Overwriting the file with help of w modifier")
f.close()

f=open("Python/Sample.txt","a")
f.write("\nWith the help of 'a' modifer we can append and then write the file")
f.close()

f=open("Python/Sample2.txt","a")
f.write("With the help of 'a' and 'w' modifer we can directly create a file too")
f.close()

f=open("Python/Sample2.txt","r+")
f.write("With the help of r+ modifier we can overwrite the file")
f.close()

# We can check everything on File I/O on stack overflow website

# with Syntax
# with open("Sample.txt","a") as f:
#       data=f.read()

with open("Python/Sample.txt","r") as f:
    data=f.read()
    print(data)     # Not necessary to close file with the help of with syntax

with open("Python/Sample.txt","a") as f:
    f.write("New data")

# Deleting a file
# using the os module
# Module(like a coding library) is a file written by another programmer that generally has functions we can use

# import os
# os.remove(filename)
import os
os.remove("Python/Sample2.txt")

# Let's Practice

# Create a new file "practice.txt" using python. Add the following data in it
# Hi everyone
# we are learning File I/O
# using Java
# I like programming in Java
with open("Python/Practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O\nusing Java\nI like programming in Java")

# WAF that replaces all occurences of Java with Python in above file
with open("Python/Practice.txt","r") as f:
    data=f.read()

new_data=data.replace("Java","Python")

with open("Python/Practice.txt","w") as f:
    f.write(new_data)

# Search if the word "learning" exists in the file or not
word="learning"
with open("Python/Practice.txt","r") as f:
    data=f.read()
    if(data.find(word)!=-1):
        print("FOUND")
    else:
        print("NOT FOUND")

# WAF to find in which line of the file does the word "learning" occur first.
# Print -1 if word not found
def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open("Practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1

        return -1
