# Words Scramble game

import random

def scramble(word):
    letters = list(word)
    random.shuffle(letters)
    return ''.join(letters)

words = ["python", "computer", "engineering", "algorithm", "network", "keyboard", "variable"]

score = 0

while True:
    word = random.choice(words)
    scrambled = scramble(word)

    print("\nScrambled word:", scrambled)

    while True:
        guess = input("Your guess (or type 'quit'): ").strip().lower()

        if guess == "quit":
            print("\nGame Over.")
            print("Your final score:", score)
            exit()

        if guess == word:
            print("Correct!")
            score += 1
            break
        else:
            print("Incorrect. Try again.")

