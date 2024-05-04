import unittest
from guess_number_game import GuessNumberGame, NumberRandomizer
from unittest.mock import patch


class TestGuessNumberGame(unittest.TestCase):

    def setUp(self):
        self.game = GuessNumberGame(NumberRandomizer())

    def test_initialization(self):
        self.assertEqual(self.game.player_name, "", "Player name is not initialized as an empty string.")
        self.assertIsNone(self.game.secret_number, "Secret number is not initialized as None.")
        self.assertEqual(self.game.guesses_left, 0, "Guesses left is not initialized as 0.")
        self.assertEqual(self.game.guesses_taken, 0, "Guesses taken is not initialized as 0.")

    def test_validate_user_input_valid(self):
        self.assertTrue(self.game.validate_user_input("10"))

    def test_validate_user_input_invalid(self):
        self.assertFalse(self.game.validate_user_input("0"))
        self.assertFalse(self.game.validate_user_input("21"))
        self.assertFalse(self.game.validate_user_input("abc"))
        self.assertFalse(self.game.validate_user_input("5.5"))

    @patch.object(NumberRandomizer, 'generate_random_number')
    def test_game_flow_correct_guess(self, mock_random_number):
        mock_random_number.return_value = 10    # Configure the mock to return a predefined number

        game = GuessNumberGame(NumberRandomizer())    # Create an instance of GuessNumberGame

        with patch('builtins.input', side_effect=['John', 'Yes', '10', 'No']):
            game.run()

        # Assert that the game behaves as expected after a correct guess
        self.assertEqual(game.player_name, 'John', "Player name is not set correctly.")
        self.assertEqual(game.secret_number, 10, "Secret number is not set correctly.")
        # Add more assertions as needed



if __name__ == '__main__':
    unittest.main()