for i in range(5, 101, 5):
    print(i, end=" ")

print()

names = ["Avanish","Awwab","Nathan"]
nicknames = ["Amar","Akbar","Anthony"]
hobbies = ["Marvel","Anime","Games"]

for name, nickname in zip(names, nicknames):
    print(f"Name: {name}, Nickname: {nickname}")

for name, nickname, hobby in zip(names, nicknames, hobbies):
    print(f"Name: {name}, Nickname: {nickname}, Hobby: {hobby}")

choice = 'y'

while choice.lower() == 'y':
    choice = input("Enter choice [y/n] : ")