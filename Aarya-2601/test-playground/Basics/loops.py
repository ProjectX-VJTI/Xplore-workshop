for i in range(0,101,5):
    print(i, end=" ")

print() #added cause styling is meh without it

for i in range(3,99,4): 
    print(i, end=" ")

print() #same reason as above

names = ["Avanish","Awwab","Nathan"]
nicknames = ["Amar","Akbar","Anthony"]

for names, nicknames in zip(names, nicknames):
    print(f"Name: {names}, Nickname:{nicknames}")

print() #added unnecessarily js for the sake of it

names = ["Avanish","Awwab","Nathan"]
nicknames = ["Amar","Akbar","Anthony"]
hobbies = ["Marvel","Anime","Games"]

for name,nickname,hobbies in zip(names, nicknames, hobbies): 
    print(f"Name:{name}, Nickname:{nickname}, Hobby:{hobbies}") 

print() #love making the code aesthetic :)

choice = 'y'
while choice.lower() == 'y':
    choice = input("Enter choice [y/n] : ")