
import random
import nltk
#nltk.download("words")
from nltk.corpus import words

def main():
    while True:
        try:
            length= int(input("Enter the length of your word between 3-10 (both inclusive): "))
            if (length <3) | (length >10):
                raise ValueError
            else:
                word_of_day = hangman(length)
                break
        except ValueError:
            print("Please enter a valid number between 3-10 (both inclusive)")
            pass
    print(guesses(word_of_day, length))


def hangman(length):
    #------ Generate random word of length "length"-------
    wordlist = words.words()
    #random.seed(30)
    while True:
        word_of_day= random.choices(wordlist)[0]
        word_of_day=word_of_day.lower()
        if len(word_of_day) == length:
            #print(word_of_day)
            break
    return word_of_day

def guesses(word_of_day,length):

    #------------Check Guesses------------
    guess= difficulty(length)
    print(f"You have total {guess} attempts")

    # Display asterisks(*) inplace of actual word
    display = '*' * length
    print (display)

    letters_guessed=[]
    while guess > 0:
        #----Validate the guessed letter-----
        letter= input("Enter a letter: ").strip().lower()
        if letter.isalpha() == False:
            print('Please enter a LETTER.')
            continue
        if len(letter) != 1:
            print('Please enter a single letter.')
            continue
        if letter in letters_guessed:
            print("You have already guessed this letter!")
            continue

        if letter in word_of_day:
            print('Correct Guess :)')
            new_display = ''
            for w, l in zip(word_of_day, display):
                if letter.lower() == w:
                    new_display += letter.lower()
                else:
                    new_display += l
            display = new_display
            print(display)
        else:
            print(f"Incorrect Guess")
            print(display)
        guess -= 1
        letters_guessed.append(letter)
        print("Attempts Remaining:", {guess})
        print("Guessed letters are: ",letters_guessed)
        #print("\n")

    #End of the Game
        if "*" not in display:
            return f"Congrats! You guessed the word correctly: {word_of_day.upper()}"
            #return
    return f"All attempts exhausted. Game Over!\n The word was: {word_of_day.upper()}"


def difficulty(length):
    while True:
        try:
            level= int(input("Enter Difficulty Level: \n 1 for Easy\n 2 for Intermediate\n"))
            if level not in [1,2]:
                raise ValueError
            elif level == 1:
                guess= length *3
                return guess
            elif level == 2:
                guess= length *2
                return guess
        except ValueError:
            pass



if __name__ == "__main__":
    main()


