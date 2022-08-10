# this is a game of guessing the age of a person that lives inside the game. User has limited attempts to guess the age, or he fails and is a loser

import random as r

secret_age = r.randint(1, 10)  # randint random integer
flag = False


def game_func(guessed_age, secret):
    if guessed_age < secret:
        return "Too low"
    elif guessed_age > secret:
        return "Too high"
    else:
        return "Correct"


# setting limited attempts
for i in range(1, 6):
    print("Take a guess. You have " + str(6 - i) + " guesses left")
    guess = input()
    if game_func(int(guess), secret_age) == 'Correct':
        print("You won the game")
        flag = True
        break
if not flag:
    print("you lost the game")
