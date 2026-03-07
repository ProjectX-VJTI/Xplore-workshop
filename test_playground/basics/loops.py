# print all multiples of 5 in [1,100]

for i in range(0,101): # start, stop, step , range is [start,stop)
    if(i%5 == 0):
        print(i,"\n")


names = ["Avanish","Awwab","Nathan"]
nicknames = ["Amar","Akbar","Anthony"]

for name,nickname in zip(names, nicknames): # wow cool new function
    print("Name:"+name +" Nickname:" + nickname + "/n") #  fill this at least

# try zip for adding this array to the above 2 and printing all 3 in loop
hobbies = ["Marvel","Anime","Games"]
for name,nickname,hobby in zip(names, nicknames , hobbies):
    print("Name:"+name +" Nickname:" + nickname +" Hobby :" + hobby)

choice = 'y'

while choice == 'y':
    choice = input("Enter choice [y/n] : ")
    # can you make this case insensitive with one more condition?



