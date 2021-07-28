# exercise!
from random import randint
from sys import argv

first = argv[1]
last = argv[2]

ran = str(randint(int(first), int(last)))

while True:
    ans = input(f"Guess the number between {first} and {last}: ")

    if ans == ran:
        print("You got it!")
        break
    else:
        print("Try again!")
