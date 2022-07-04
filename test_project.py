from unittest import mock
from unittest import TestCase
from project import hangman, difficulty, guesses
import random


class DifficultyTests(TestCase):
    @mock.patch('project.input', create=True)
    def test_difficulty(self, mocked_input):
        mocked_input.side_effect = ["1"]
        result = difficulty(5)
        self.assertEqual(result, 10)

class HangmanTests(TestCase):
    def test_hangman(self):
        random.seed(30)
        result = hangman(5)
        self.assertEqual(result, "flosh")

class GuessesTests(TestCase):
    @mock.patch('project.input', create=True)
    def test_guesses(self, mocked_input):
        random.seed(30)
        mocked_input.side_effect = [1,"a","f","l","o","s","h"]
        result = guesses("flosh",5)
        self.assertEqual(result, f"Congrats! You guessed the word correctly: FLOSH")
