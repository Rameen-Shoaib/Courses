import random
import sys

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        pass

while True:
    try:
        check =  random.randint(1, n)

        while True:
            guess = int(input("Guess: "))
            if guess > 0:
                break

        if guess < check:
            print("Too small!")
        elif guess > check:
            print("Too large!")
        else:
            print("Just right!")
            sys.exit()

    except ValueError:
        pass