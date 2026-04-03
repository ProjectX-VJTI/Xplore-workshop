# print all multiples of 5 in [1,100]

for i in range(5, 101, 5): # start,end, step by 5
    print(i, end=" ")


names = ["Avanish","Awwab","Nathan"]
nicknames = ["Amar","Akbar","Anthony"]
hobbies = ["Marvel","Anime","Games"] # try zip for adding this array to the above 2 and printing all 3 in loop
    
for name,nickname,hobby in zip(names, nicknames, hobbies): # wow cool new function
    print(f"Name: {name}, Nickname: {nickname}, Hobby: {hobby}") #  fill this at least



choice = 'y'

while choice == 'y': # can you make this case insensitive with one more condition?
    choice = input("Enter choice [y/n] : ").lower()

