# Battleship Game
import random

ships = random.sample(range(1, 10), 3)   # 3 ship positions
found = 0
guessed = []
attempts = 0

while found < 3:
    guess = int(input("Guess (1-9): "))

    if guess < 1 or guess > 9:
        print("Out of range")
        continue

    if guess in guessed:
        print("Already guessed")
        continue

    guessed.append(guess)
    attempts += 1

    if guess in ships:
        print("HIT!")
        found += 1
    else:
        print("MISS!")

print("All ships destroyed")
print("Attempts:", attempts)


