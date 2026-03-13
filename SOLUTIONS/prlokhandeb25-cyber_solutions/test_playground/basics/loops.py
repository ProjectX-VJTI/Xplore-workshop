# print all multiples of 5 in [1,100]
for n in range(1,21):
    print(n*5,end=" ")
print()
for i in range(5,105,5): # start, stop, step , range is [start,stop)
    print(i,end=" ")
    
print()
names = ["Avanish","Awwab","Nathan"]
nicknames = ["Amar","Akbar","Anthony"]
hobbies = ["Marvel","Anime","Games"]

for name, nickname, hobby in zip(names, nicknames, hobbies):
    print(f"Name:{name}, Nickname:{nickname}, Hobby:{hobby} ")




choice = 'y'

while choice.lower() == 'y': # can you make this case insensitive with one more condition?
    choice = input("Enter choice [y/n] : ")
