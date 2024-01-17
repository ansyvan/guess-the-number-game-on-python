import unittest
from guess_number_game import GuessNumberGame
from unittest.mock import patch

class TestGuessNumberGame(unittest.TestCase):   # Create testing class that subclasses 'TestCase' class within the 'unittest' module.

    def test_initialization(self):
        game = GuessNumberGame()    # Create an instance of the GuessNumberGame class
        self.assertIsInstance(game, GuessNumberGame, "The object is not an instance of GuessNumberGame.")
        self.assertEqual(game.player_name, "", "Player name is not initialized as an empty string.")
        self.assertIsNone(game.secret_number, "Secret number is not initialized as None.")
        self.assertEqual(game.guesses_left, 0, "Guesses left is not initialized as 0.")
        self.assertEqual(game.guesses_taken, 0, "Guesses taken is not initialized as 0.")

    def test_generate_secret_number(self):
        game = GuessNumberGame()
        secret_number = game.generate_secret_number()
        self.assertTrue(game.MIN_NUMBER <= secret_number <= game.MAX_NUMBER)

if __name__ == '__main__':
    unittest.main()
