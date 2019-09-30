"""
Plays a simple guessing game with the user, with numbers 0-9
William Alber 9/19/2019
"""
from random import randint
random_num = randint(0,100)

# Starts a loop to test guesses efficiently
print("Welcome to my guessing game! I hope you enjoy.")
print("You have to try and guess my number between 0-100!\n")
test = False
while not test:
    # Loop will run until number is guessed
    guess = int(input("What is your guess: "))
    if guess == random_num:
        print("You guessed my number! Nice job!")
        test = True # breaks us out of loop
    elif guess < random_num:
        print("Guess Higher!\n")
    elif guess > random_num:
        print("Guess Lower!\n")
    else:
        print("Try again!")
