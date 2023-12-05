# This is a guess the number game

import random

print("Hello. What is your name?")
name = input()

print("Well, " + name + ", I am thinking of a number between 1 and 20.")
secretNumber = random.randint(1, 20)

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):

    guessesLeft = 7 - guessesTaken
    if guessesLeft != 1:
        print("Take a guess. You have " + str(guessesLeft) + " guesses left.")
    else:
        print("Take a guess. You have " + str(guessesLeft) + " guess left.")

    guess = input()
    try:
        if 0 < int(guess) < 21:
            if int(guess) < secretNumber:
                print("Your number is too low. ")
            elif int(guess) > secretNumber:
                print("Your number is too high. ")
            else:
                break   # This condition is the correct guess!
        else:
            print("Your number should be between 1 and 20.")
    except ValueError:
        print("Please, enter an integer number.")

if int(guess) == secretNumber:
    if guessesTaken == 1:
        print("Wow, " + name + "! You made it in the first try!")
    else:
        print("Good job, " + name + "! You guessed my number in " + str(guessesTaken) + " guesses!")
else:
    print("Nope. The number I was thinking of was " + str(secretNumber) + " .")