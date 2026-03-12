# print all multiples of 5 in [1,100]
for i in range (0, 101, 5): print(i, end=" ")

for i in range(3,99,4): # start, stop, step , range is [start,stop)
    print(i,end=" ")

print('\n')
names = ["Avanish","Awwab","Nathan"]
nicknames = ["Amar","Akbar","Anthony"]
hobbies = ["Marvel","Anime","Games"]
for name,nickname,hobby in zip(names, nicknames, hobbies): # wow cool new function
    print(f"Name: {name},  Nickname: {nickname}, Hobby: {hobby}") #  fill this at least

# try zip for adding this array to the above 2 and printing all 3 in loop

choice = 'y'

while choice.lower() == 'y' or choice.lower()=='yes': # can you make this case insensitive with one more condition?
    choice = input("Enter choice [y/n] : ")