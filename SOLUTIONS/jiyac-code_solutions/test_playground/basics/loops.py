# print all multiples of 5 in [1,100]

for i in range(5,101,5): # start, stop, step , range is [start,stop)
    print(i,end=" ")

print('\n')

names = ["Avanish","Awwab","Nathan"]
nicknames = ["Amar","Akbar","Anthony"]
hobbies = ["Marvel","Anime","Games"] # try zip for adding this array to the above 2 and printing all 3 in loop

for name,nickname,hobby in zip(names, nicknames,hobbies): # wow cool new function
    print(f"Name:  {name},  Nickname: {nickname},  Hobbies: {hobby}") #  fill this at least


choice = 'y'

while choice == 'y' or choice=='Y': # can you make this case insensitive with one more condition?
    choice = input("Enter choice [y/n] : ")

