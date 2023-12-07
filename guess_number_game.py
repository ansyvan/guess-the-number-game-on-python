# This is a guess the number game

import random
import sys

class GuessNumberGame:
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    MAX_GUESSES = 9

    def __init__(self):
        self.name = ""

    def hello(self):
        print("Hello there! May I know your name?")
        self.name = input()
        self.ask_to_play()
    
    def ask_to_play(self):
        print(f"Welcome, {self.name}, to the 'Guess the Number' game! Would you like to play? (Yes/No)")
        self.make_choise()

    def make_choise(self):
        answer_yes_no = input().lower()
        if answer_yes_no == "yes":
            self.play_guess_number()
        elif answer_yes_no == "no":
            print("I feel sorry to hear that. Hope to see you again soon.")
            self.exit_game()
        else:
            print("Please type either 'Yes' or 'No'")
            self.make_choise()

    def play_guess_number(self):
        print(f"Well, {self.name}, I am thinking of a number between {self.MIN_NUMBER} and {self.MAX_NUMBER}.")
        self.secret_number = random.randint(self.MIN_NUMBER, self.MAX_NUMBER)

        # Ask the player to guess a limited number of times.
        for i in range(1, self.MAX_GUESSES):
            self.guesses_taken = i
            self.guesses_left = self.MAX_GUESSES - self.guesses_taken

            # Display appropriate message based on remaining guesses.
            if self.guesses_left == self.MAX_GUESSES - 1:
                print(f"Take a guess! You have {self.guesses_left} guesses left.")
            elif self.guesses_left != 1:
                print(f"Try again! You have {self.guesses_left} guesses left.")
            else:
                print(f"Try again! You have {self.guesses_left} guess left.")
        
            self.validate_data()    # Validate the user's input.

            # Check if the guessed number is correct.
            if self.check_guess(self.guess):
                break   # Exit the loop if the guess is correct.
        
        self.game_result(self.guess)

    # Validating the input data
    def validate_data(self):
        while True:
            self.guess = input()
            try:
                self.guess = int(self.guess)
                if self.MIN_NUMBER <= self.guess <= self.MAX_NUMBER:
                    return self.guess    # Return the validated guess
                else:
                    print(f"Your number should be between {self.MIN_NUMBER} and {self.MAX_NUMBER}.")
            except ValueError:
                print("Please, enter an integer number.")

    # Check if the number is correct
    def check_guess(self, guess):
        self.guess = guess
        if self.guess < self.secret_number:
            print("Your number is too low.")
        elif self.guess > self.secret_number:
            print("Your number is too high.")
        else:
            self.game_result(guess)  # This condition is the correct guess!
            return True
            
    # Resuls of the game
    def game_result(self, guess):
        self.guess = guess
        if self.guess == self.secret_number:
            if self.guesses_taken == 1:
                print(f"Wow, {self.name}! You made it in the first try!")
            else:
                print(f"Good job, {self.name}! You guessed my number in {self.guesses_taken} guesses!")
        else:
            print(f"No guesses left. The number I was thinking of was {self.secret_number}.")
        
        self.ask_to_play_again()

    def ask_to_play_again(self):
        print("Play again? (Yes/No)")
        self.make_choise()

    def exit_game(self):
        sys.exit()

game = GuessNumberGame()
game.hello()