import random
import sys

class NumberRandomizer:
    MIN_NUMBER = 1
    MAX_NUMBER = 20

    @staticmethod
    def generate_random_number():
        return random.randint(NumberRandomizer.MIN_NUMBER, NumberRandomizer.MAX_NUMBER)

class GuessNumberGame:
    MAX_GUESSES = 5

    def __init__(self, randomizer):
        self.player_name = ""
        self.secret_number = None
        self.guesses_left = 0
        self.guesses_taken = 0
        self.randomizer = randomizer


    # Beginning with asking the Player's name
    def run(self):
        print("Hello there! May I know your name?")
        player_name = input()
        print(f"Welcome, {player_name}, to the 'Guess the Number' game! Would you like to play? (Yes/No)")
        if self.get_user_yes_no_input():    # Check if the player wants to play
            while True:     # If the player wants to play, enter a loop for the game
                self.play(player_name)      # Start the game
                print("Play again? (Yes/No)")   # After finishing the game, ask if the player wants to play again
                if not self.get_user_yes_no_input():    # Check if the player wants to play again
                    break       # If "No", exit the loop. If "Yes," the loop continues.
            self.exit_game()


    # Answering any Yes/No questions
    def get_user_yes_no_input(self):
        while True:
            answer_yes_no = input().lower()
            if answer_yes_no == "yes":
                return True
            elif answer_yes_no == "no":
                print("I feel sorry to hear that. Hope to see you again soon.")
                return False
            else:
                print("Please type either 'Yes' or 'No'")

        
    # def generate_secret_number(self):
    #     self.secret_number = self.randomizer.generate_random_number()
    #     return self.secret_number


    # Display appropriate message on remaining guesses.
    def display_remaining_guesses(self, guesses_left):
        if guesses_left == self.MAX_GUESSES:
            print(f"Take a guess! You have {self.MAX_GUESSES} tries.")
        elif guesses_left != 1:
            print(f"Try again! You have {guesses_left} guesses left.")
        else:
            print(f"Try again! You have {guesses_left} guess left.")


    def calculate_guesses_left(self, guesses_taken):
        self.guesses_left = (self.MAX_GUESSES + 1) - guesses_taken
        return self.guesses_left
    

    def read_user_guess(self):
        guess = None
        guess_is_valid = False
        while not guess_is_valid:
            guess = input()
            guess_is_valid = self.validate_user_input(guess)
        return int(guess)
        
        
    # Validate the input data is integer from MIN to MAX number
    def validate_user_input(self, guess):
        try:
            guess = int(guess)
            if NumberRandomizer.MIN_NUMBER <= guess <= NumberRandomizer.MAX_NUMBER:
                return True    # Return the validated guess
            else:
                print(f"Your number should be between {NumberRandomizer.MIN_NUMBER} and {NumberRandomizer.MAX_NUMBER}.")
        except ValueError:
            print("Please, enter an integer number.")


    # Check if the number is correct
    def check_guess(self, guess, secret_number):
        if guess < secret_number:
            print("Your number is too low.")
            return False
        elif guess > secret_number:
            print("Your number is too high.")
            return False
        else:
            return True  # This condition is the correct guess!
            
            
    # Resuls of the game when Player guesses or loop is over
    def game_result(self, player_name, guess, secret_number, guesses_taken):
        if guess == secret_number:
            if guesses_taken == 1:
                print(f"Wow, {player_name}! You made it in the first try!")
            else:
                print(f"Good job, {player_name}! You guessed my number in {guesses_taken} guesses!")
        else:
            print(f"No guesses left. The number I was thinking of was {secret_number}.")

        
    def play(self, player_name):
        print(f"Well, {player_name}, I am thinking of a number between {NumberRandomizer.MIN_NUMBER} and {NumberRandomizer.MAX_NUMBER}.")
        secret_number = self.randomizer.generate_random_number()
        guess = 0
        for guesses_taken in range (1, self.MAX_GUESSES + 1):
            guesses_left = self.calculate_guesses_left(guesses_taken)

            self.display_remaining_guesses(guesses_left)
            guess = self.read_user_guess()

            # Check if the guessed number is correct
            if self.check_guess(guess, secret_number):
                break   # Exit the loop if the guess is correct

        self.game_result(player_name, guess, secret_number, guesses_taken)


    def exit_game(self):
            sys.exit()

if __name__ == "__main__":
    randomizer = NumberRandomizer()
    game = GuessNumberGame(randomizer)
    game.run()