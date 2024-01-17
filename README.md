# python_projects

1. [Guess the Number Game](https://github.com/ansyvan/python_projects/blob/main/guess_number_game.py)

This is a simple Python-based "Guess the Number" game designed to run in the console. The game generates a random number between a specified range, and the player has a limited number of attempts to guess the correct number.

<b>How to Play</b>

- Run the script in a Python environment.
- Enter your name when prompted.
- The game will generate a random number between `1` and `20`.
- You have up to `5` attempts to guess the correct number.
- After each guess, the game will provide feedback on whether the guess is too high, too low, or correct.
- The game ends when the correct number is guessed or when no attempts are left.
- You can choose to play the game again if you wish.

<b>Features</b>

- The `secret_number` is randomly generated using `random` module.
- User-friendly interface with clear instructions. The `player_name` variable is reused multiple times.
- Input field validation.
- Interactive feedback on each guess. The program informes the User about the number of guesses left.
- Ability to replay the game multiple times.

<b>Game Logic</b>

The game is implemented using Python and includes a simple class `GuessNumberGame` to encapsulate the game logic. The player is prompted for input, and the program validates and processes the guesses. The game provides real-time feedback, keeping the player engaged throughout the process.

<b>The Input Field validation:</b> An input field accepts only integer numbers in a certain range.

- A valid number is an integer number in a range between the minimal and the maximum number defined by a program.
- A valid right number is an integer number defined randomly by a program as a `secret_number`.
- A valid wrong number is an integer number that is in the range between `min` and `max` but does not equal the `secret_number`.
- An invalid datatype is a `float`, `text`, `symbol`, or `space`.

The <b>result</b> of the Game have three scenarios:

- The User was lucky to guess the number on the first try.
- The User guessed the secret number within the given number of guesses.
- The User has no guesses left so they lose.
