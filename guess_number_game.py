# This is a guess the number game

import random
import sys

class GuessNumberGame:
    MIN_NUMBER = 1
    MAX_NUMBER = 20
    MAX_GUESSES = 6

    def __init__(self):
        pass
    
    # Beginning with asking the Player's name
    def ask_player_name(self):
        print("Hello there! May I know your name?")
        self.player_name = input()
        return self.player_name

    def run(self):
        print(f"Welcome, {self.player_name}, to the 'Guess the Number' game! Would you like to play? (Yes/No)")
        

    # Answering any Yes/No questions
    def yes_no_choise(self):
        self.answer_yes_no = input().lower()
        if self.answer_yes_no == "yes":
            self.play_guess_number()
        elif self.answer_yes_no == "no":
            print("I feel sorry to hear that. Hope to see you again soon.")
            self.exit_game()
        else:
            print("Please type either 'Yes' or 'No'")
            self.yes_no_choise()
        return self.answer_yes_no
        

    def generate_secret_number(self):
        print(f"Well, {self.player_name}, I am thinking of a number between {self.MIN_NUMBER} and {self.MAX_NUMBER}.")
        self.secret_number = random.randint(self.MIN_NUMBER, self.MAX_NUMBER)


    # Display appropriate message on remaining guesses.
    def display_remaining_guesses(self):
        for self.guesses_left in range(1, self.MAX_GUESSES):
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

    def calculate_guesses_left(self):
            self.guesses_left = self.MAX_GUESSES - self.guesses_taken
            return self.guesses_left
    



    def read_user_guess(self):
        if self.guess == False:
            self.guess = input()
            self.validate_input_data()
        else:
            return self.guess
        



    # Validate the input data is integer from MIN to MAX number
    def validate_input_data(self):
        while True:
            self.guess = input()
            try:
                self.guess = int(self.guess)
                if self.MIN_NUMBER <= self.guess <= self.MAX_NUMBER:
                    return True    # Return the validated guess
                else:
                    print(f"Your number should be between {self.MIN_NUMBER} and {self.MAX_NUMBER}.")
            except ValueError:
                print("Please, enter an integer number.")

    # Check if the number is correct
    def check_guess(self):
        if self.guess < self.secret_number:
            print("Your number is too low.")
        elif self.guess > self.secret_number:
            print("Your number is too high.")
        else:
            self.game_result(self.guess)  # This condition is the correct guess!
            return True
            
    # Resuls of the game when Player guesses or loop is over
    def game_result(self):
        if self.guess == self.secret_number:
            if self.guesses_taken == 1:
                print(f"Wow, {self.player_name}! You made it in the first try!")
            else:
                print(f"Good job, {self.player_name}! You guessed my number in {self.guesses_taken} guesses!")
        else:
            print(f"No guesses left. The number I was thinking of was {self.secret_number}.")
        

    def ask_to_play_again(self):
        print("Play again? (Yes/No)")
        self.yes_no_choise()

    def exit_game(self):
        sys.exit()

game = GuessNumberGame()
game.run()