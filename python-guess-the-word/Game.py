import os
import random

from ComputerWords import dictionary

# Initialize the game values
word_to_guess = ""          
user_guesses = []           # Stores all the user guesses
wrong_guesses = []          # Stores all the wrong guesses
word_is_guessed = False     # Used to determine if user has successfully guessed the word  
chances = 5                 # Number of mistakes the user is allowed to make

def main():
    playGame()

    # Ask the user for a new game
    try_again = input("\nWould you like to try again? [y/n]: ")

    while try_again == "y" or try_again == "yes":
        os.system('cls')    # Clears the screen
        playGame()  
        try_again = ""      # Clear the previous input
        try_again = input("\nWould you like to try again? [y/n]: ")


def initialiseGame():   # Resets the game variables for a new game
    global word_to_guess, user_guesses, wrong_guesses, word_is_guessed, chances
    words = list(dictionary.keys())         # Make a list of the keys (which are the words) from the dictionary
    word_to_guess = random.choice(words)    # Randomly choose a word from a file
    user_guesses = []                       # Stores all the user guesses
    wrong_guesses = []                      # Stores all the wrong guesses
    word_is_guessed = False                 # Used to determine if user has successfully guessed the word  
    chances = 5                             # Number of mistakes the user is allowed to make

def validateInput(user_input):  # Validates the user input before accepting guess
    valid = True

    # Only accept one character and it must be a letter
    if len(user_input) > 1:
        print("Please only input one character.")
        valid = False
    elif not user_input.isalpha():
        print("Please input a letter.")
        valid = False

    return valid

def showGameLogo():
    print("""\

   _____                          _   _                                     _ 
  / ____|                        | | | |                                   | |
 | |  __ _   _  ___  ___ ___     | |_| |__   ___     __      _____  _ __ __| |
 | | |_ | | | |/ _ \/ __/ __|    | __| '_ \ / _ \    \ \ /\ / / _ \| '__/ _` |
 | |__| | |_| |  __/\__ \__ \    | |_| | | |  __/     \ V  V / (_) | | | (_| |
  \_____|\__,_|\___||___/___/     \__|_| |_|\___|      \_/\_/ \___/|_|  \__,_|
                                                                              
                                                                              
                    """)
    # Want to print your own ASCII text art? Visit https://patorjk.com/software/taag/

def printWord():    # Used to clear the screen and display the word and missing letters accordingly
    os.system('cls')

    showGameLogo()

    # Show the letter in the word if the guess is in the word
    # Else, show a blank or underscore
    for character in word_to_guess:
        if character in user_guesses:
            print(character, end=" ")
        elif character == " ":
            print(" ", end=" ")
        elif character == "-":
            print("-", end=" ")
        else:
            print("_", end=" ")
    
    # Display the incorrect letters
    print("\n\nIncorrect guesses: ")
    print(wrong_guesses)
    print("Chances left: " + str(chances))

def playGame():     # Main function containing game logic
    initialiseGame()
    printWord()

    global chances
    global word_is_guessed
    global remaining_letters

    while chances > 0 and word_is_guessed == False:
        guess = input("\nGuess: ")
        isValidInput = validateInput(guess)

        while not isValidInput:
            guess = input("Guess: ")
            isValidInput = validateInput(guess)

        # Force the user guess to be lower case
        guess = guess.lower()

        # Guesses need to be unique so only add the guess if it hasn't been used
        if guess not in user_guesses:
            user_guesses.append(guess)     
            if not guess in word_to_guess:
                wrong_guesses.append(guess)
                chances = chances - 1

            printWord()
        else:
            printWord()
            print("You already guessed this letter.")

        # Check if word is correctly guessed
        # We are using the set() function to check if the letters in the user_guesses exist in the word_to_guess
        # Not familiar with sets? Here's a simple article explaining sets (https://www.mathsisfun.com/sets/sets-introduction.html)
        # Programming uses a lot of math concepts so programmers need to be mathematical thinkers as well :)
        # We also used the replace() function so we don't need to worry about spaces and dashes in word. We just want the letters.
        if(set(word_to_guess.lower().replace(" ", "").replace("-", "")).issubset(set(user_guesses))):
            word_is_guessed = True

    if chances == 0:
        print("You run out of chances. The word was: " + word_to_guess)
    
    if word_is_guessed == True:
        print("Congratulations! You guessed the word!")
    
    print("\n")
    print(word_to_guess + " - " + dictionary[word_to_guess])

# Start with the main() function     
if __name__ == "__main__":
    main()
