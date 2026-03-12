# print all multiples of 5 in [1,100]

## FIX:
for i in range(0,101,5): # start, stop, step , range is [start,stop)
    if(i == 0):
        continue
    print(i,end=" ")


names = ["Avanish","Awwab","Nathan"]
nicknames = ["Amar","Akbar","Anthony"]

##FIX:
for name,nickname in zip(names, nicknames): # wow cool new function
    print(f"Name: {name}, Nickname: {nickname}") #  fill this at least

# try zip for adding this array to the above 2 and printing all 3 in loop
hobbies = ["Marvel","Anime","Games"]

choice = 'y'

##FIX : added case for 'Y'
while choice == 'y' or choice == 'Y': # can you make this case insensitive with one more condition?
    choice = input("Enter choice [y/n] : ")

