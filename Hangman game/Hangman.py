# This is a HANGMAN game. You will be given any random word to guess,letter-by-letter.

#import the libraries

import random
from words import word_list

#generate a random word based on dictionary
def get_word():
    word = random.choice(word_list)
    return word.upper()

def play_game(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Be ready to play the game. ")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

#enter the loop to start the game
    while not guessed and tries > 0:
        guess = input("Guess the letter or word: ").upper()

#the conditions says either the guess should be of a letter or it should only be an alphabet
        if len(guess) == 1 or guess.isalpha():
#condition if the guessed letter is already guessed or not
            if guess in guessed_letters:
                print("You have already guessed this letter: ",guess)
            elif guess not in guessed_letters:
                print(guess,"is not in the word. ")
                tries -= 1
            else:
                print("Good job! ",guess, "is in word. ")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i,letter in enumerate(word) if letter == guess]

                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)

                if "_" not in word_completion:
                    guessed=True


#if the guess is word and alphabet
        elif len(guess) == len(word) or guess.isalpha():
            if guess in guessed_words:
                print("You have already guessed the word: ",guess)
            elif guess != word:
                print(Guess ,"is not in the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

#any other input in invalid
        else:
            print("Not a valid input. Try again! ")

#now print or display the result after the loop ends
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play_game(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play_game(word)


if __name__ == "__main__":
    main()