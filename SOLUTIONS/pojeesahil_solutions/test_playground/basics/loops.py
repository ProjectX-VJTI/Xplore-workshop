# print all multiples of 5 in [1,100]

for i in range(5,101,5): # start, stop, step , range is [start,stop)
    print(i,end=" ")
print("")

names = ["Avanish","Awwab","Nathan"]
nicknames = ["Amar","Akbar","Anthony"]
hobbies = ["Marvel","Anime","Games"]

for name,nickname,hobbies in zip(names, nicknames,hobbies): # wow cool new function
    print("Name:",name,  "  Nickname:",nickname,"  Hobby:",hobbies) #  fill this at least

# try zip for adding this array to the above 2 and printing all 3 in loop


choice = 'y'

while choice.lower() == 'y': # can you make this case insensitive with one more condition?
    num=int(input("Try to think a number and then enter it here, I will try to guess it...\n"))
    print("Was your number ",num, ", See i am so smart that i guessed it haha")
    choice = input("Enter choice [y/n] : ")

