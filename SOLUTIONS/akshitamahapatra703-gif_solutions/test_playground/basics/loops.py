# print all multiples of 5 in [1,100]

# [1, 100] means 100 is included, so we use 101 as the stop value
for i in range(5, 101, 5): 
    print(i, end=" ")
print() 

names = ["Avanish", "Awwab", "Nathan"]
nicknames = ["Amar", "Akbar", "Anthony"]
hobbies = ["Marvel", "Anime", "Games"]

# Zipping all three lists together
for name, nickname, hobby in zip(names, nicknames, hobbies):
    print(f"Name: {name}, Nickname: {nickname}, Hobby: {hobby}")

choice = 'y'

# .lower() makes 'Y' become 'y', satisfying the condition
while choice.lower() == 'y': 
    choice = input("Enter choice [y/n] : ")

