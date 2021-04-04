import random

randNum = random.randint(0,100)

def guess():
    num = int(input("Guess: "))

    if num == randNum:
        print("*-*-*-*-*-*-*-*-*-*-*-*")
        print("That was right!")
        print(f"No:{num}")
        print("*-*-*-*-*-*-*-*-*-*-*-*")
    elif num < randNum:
        print("Wrong, number should be greater")
        print(f"Last guess: {num}")
        print("---------------------")
        return guess()
    elif num > randNum:
        print("Wrong, number should be less")
        print(f"Last guess: {num}")
        print("---------------------")
        return guess()

guess()