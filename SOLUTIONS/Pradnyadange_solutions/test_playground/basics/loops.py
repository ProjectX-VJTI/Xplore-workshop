# print all multiples of 5 in [1,100]

for i in range(1,101,1): # start, stop, step , range is [start,stop)
    if i%5 == 0:
     print(i,end=" ")
print('\n')

names = ["Avanish","Awwab","Nathan"]
nicknames = ["Amar","Akbar","Anthony"]

for name,nickname in zip(names, nicknames): # wow cool new function
    print(f"Name: {name}, Nickname: {nickname}") #  fill this at least

# try zip for adding this array to the above 2 and printing all 3 in loop
hobbies = ["Marvel","Anime","Games"]
for name,nickname,hobby in zip(names, nicknames,hobbies):
 print(f"Name: {name}, Nickname: {nickname}, Hobby : {hobby}")
choice = 'y'

while choice == 'y'or choice == 'Y': # can you make this case insensitive with one more condition?
    choice = input("Enter choice [y/n] : ")
