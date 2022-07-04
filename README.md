# Project HANGMAN by Gargi Nirmal from Munich (Germany)

### Description:
The program is like the Hangman game with a few modifications which are mentioned in each of the functions below.
The user gets to select the length of the word that she would like to guess. The user is then prompted to select the difficulty level of the game. The number of attempts that the user gets to guess the word are (length of the word) * 2 for Intermediate level and (length of the word) * 3 for Easy level. The user then has to guess one letter at a time until: either user guesses the word correctly, or the user exhausts all the attempts. There are some sanity checks to validate the input letters: for example it should only be a letter between a-z, there cannot be more than one letter at a time etc.<br>
Apart from all the usual libraries, one additional library needs to be installed: `nltk`
-
### Video Demo:  <https://youtu.be/7ha2dyuecpY>
### Files:
    project.py
Contains all the functionality<br>
    test_project.py
Contains unit tests for each individual function used in `project.py`<br>
    requirements.txt
Contains all libraries that must be installed before executing the project.

### Functions:
    hangman()
Given an argument `length` which is any integer value between 3 and 10 (both inclusive). This function returns a random word of that length after converting it into lower case.

    guesses()
Takes 2 arguments: `word_of_day` and `length`. `word_of_day` is the random word generated by `hangman()` and `length` is its length (literally). This function checks for each guess made by the user.
When a user makes a guess by inputting a letter, this program initially makes sanity checks on the letter- if it is indeed a letter, if it is a single letter, if it is not a letter that has already been guessed.
After doing the basic sanity checks, the function then checks if the letter is present in the word. It then exposes the correct letter in the word and its position. It then subtracts one attempt.
If the user correctly guesses the word, the program informs the user and exits.
If the user is not able to guess the word and exahusts all attempts, the program informs the user and exits.

    difficulty()
The function takes `length` as input and returns the number of guesses that are allowed to the user. It asks the user which Difficulty level would the user like to play with and then accordingly returns the number of guesses allowed.