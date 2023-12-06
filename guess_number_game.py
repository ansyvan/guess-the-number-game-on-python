# This is a guess the number game

import random, sys

class GuessNumber:

    def __init__(self):
        self.name = ""

    def hello(self):
        print("Hello there! May I know your name?")
        self.name = input()
        self.ask_to_play()
    
    def ask_to_play(self):
        print("Welcome, {}, to the 'Guess the Number' game. Would you like to play? (Yes/No)".format(self.name))
        self.make_choise()

    def ask_to_play_again(self):
        print("Play again? (Yes/No)")
        self.make_choise()

    def make_choise(self):
        answer_yes_no = input().lower()
        if answer_yes_no == "yes":
            self.play_guess_number()
        elif answer_yes_no == "no":
            print("I feel sorry to hear that. Hope to see you again soon.")
            sys.exit()
        else:
            print("Please type either 'Yes' or 'No'")
            self.make_choise()

    def play_guess_number(self):
        print("Well, {}, I am thinking of a number between 1 and 20.".format(self.name))
        secret_number = random.randint(1, 20)

        # Ask the player to guess 6 times.
        for guesses_taken in range(1, 7):
            guesses_left = 7 - guesses_taken
            if guesses_left == 6:
                print("Take a guess! You have {} guesses left.".format(str(guesses_left)))
            elif guesses_left != 1:
                print("Try again! You have {} guesses left.".format(str(guesses_left)))
            else:
                print("Try again! You have {} guess left.".format(str(guesses_left)))

            guess = input()
            try:
                if 0 < int(guess) < 21:
                    if int(guess) < secret_number:
                        print("Your number is too low. ")
                    elif int(guess) > secret_number:
                        print("Your number is too high. ")
                    else:
                        break   # This condition is the correct guess!
                else:
                    print("Your number should be between 1 and 20.")
            except ValueError:
                print("Please, enter an integer number.")

        if guess == secret_number:
            if guesses_taken == 1:
                print("Wow, {}! You made it in the first try!".format(self.name))
            else:
                print("Good job, {}! You guessed my number in {} guesses!".format(self.name, (str(guesses_taken))))
        else:
            print("Nope. The number I was thinking of was {}.".format(str(secret_number)))
        self.ask_to_play_again()

game = GuessNumber()
game.hello()