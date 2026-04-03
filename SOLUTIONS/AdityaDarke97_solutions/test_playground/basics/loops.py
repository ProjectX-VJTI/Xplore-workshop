# print all multiples of 5 in [1,100]

for i in range(0,101,5): # start, stop, step , range is [start,stop)
    if i==0:
        continue
    else:
        print(i,end=" ")


names = ["Avanish","Awwab","Nathan"]
nicknames = ["Amar","Akbar","Anthony"]

for name,nickname in zip(names, nicknames): # wow cool new function
    print(f"Name:  {name} , Nickname: {nickname}") #  fill this at least

# try zip for adding this array to the above 2 and printing all 3 in loop
hobbies = ["Marvel","Anime","Games"]

choice = 'y'

while choice == 'y': # can you make this case insensitive with one more condition?
    choice = input("Enter choice [y/n] : ")

