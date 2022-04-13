import random
import os

# You can change the file name and use this quiz program for your other subjects.
# For example, you can make a quiz for your Science class. 
# You duplicate the PythonQuestions file, remove the existing questions but one, replace the content inside the quotation marks, then add more as you go.
# Then change the line below to match your new file containing new questions :)
from PythonQuestions import questions_list

class Question:
   def __init__(self, question, choices, answer, feedback):
       self._question = question
       self._choices = choices
       self._answer = answer
       self._feedback = feedback


# Initialize values
score = 0
questions = []
max_num_questions = 3

for item in questions_list:
    questions.append(Question(item["question"], item["choices"], item["answer"], item["feedback"]))

# MAIN Function   
def main():
    playGame()

     # Ask the user for a new game
    try_again = input("\nWould you like to try again? [y/n]: ")

    # Keep asking the player
    while try_again == "y" or try_again == "yes":
        os.system('cls')    # Clears the screen
        playGame()
        try_again = ""      # Clears the previous input
        try_again = input("\nWould you like to try again? [y/n]: ")

# Validate the user input
def validate(user_input):
   # Only accept a, b, c, or d
   if user_input == "a" or user_input == "b" or user_input == "c" or user_input == "d":
      valid = True
   else:
      print("That's an invalid input. You just need to choose from a, b, c, or d.")
      valid = False

   return valid

def showQuizLogo():
    print("""\

  ,                             _                           , __           _                  
 /|   /                        (_|   |                     /|/  \         | |                 
  |__/   _  _    __              |   |  __          ,_      |___/     _|_ | |     __   _  _   
  | \   / |/ |  /  \_|  |  |_    |   | /  \_|   |  /  |     |    |   | |  |/ \   /  \_/ |/ |  
  |  \_/  |  |_/\__/  \/ \/       \_/|/\__/  \_/|_/   |_/   |     \_/|/|_/|   |_/\__/   |  |_/
                                    /|                              /|                        
                                    \|                              \|                                                                            
                                                                              
                    """)

# Play game - Contains the main logic of the game
def playGame():
    global score, questions, max_num_questions

    score = 0
    # Introduction
    showQuizLogo()
    name = input("\nWhat is your name? ")
    print("\nWelcome " + name + "!")
    max_num_questions = input("We have " + str(len(questions_list)) + " questions for you. How many do you want to try out? ")

    # Only accept numbers
    while not max_num_questions.isdigit():
        max_num_questions = input("You didn't give a number, " + name + ". Try again: ")

    max_num_questions = int(max_num_questions)

    # Validate the input for number of questions
    while not str(max_num_questions).isdigit() or int(max_num_questions) > len(questions_list) or int(max_num_questions) < 2:
        if not str(max_num_questions).isdigit():
            max_num_questions = input("You didn't give a number, " + name + ". Try again: ")
        elif int(max_num_questions) > len(questions_list):
            max_num_questions = input("Oh, we don't have that many questions, " + name + ". Try again: ")
        elif int(max_num_questions) < 2:
            max_num_questions = input("Aww.. You need to answer at least 2 questions, " + name + ". Try again: ")

    # Make sure the user input converted into a number
    max_num_questions = int(max_num_questions)

    # Makes sure the questions are random for every game
    random.shuffle(questions)

    # Trim the questions to the maximum number of questions
    final_questions = questions[:max_num_questions]

    os.system('cls')    # Clears the screen

    showQuizLogo()

    print("Alright! Ready, " + name + "? Here's your first question: \n")

    for question in final_questions:
        print("""{}""".format(question._question))
        print("""{}""".format(question._choices))
        answer = input("\nEnter your guess: ")

        # Validate the user input
        valid = validate(answer)
        while not valid:
           answer = input("Try another guess: ")
           valid = validate(answer)
            
        if(answer == question._answer):
            print("\nCorrect!", end=" ")
            score += 1
        else:
            print("\nOops.. The correct answer is " + question._answer + ".")
        
        print(question._feedback)

        input()
        os.system('cls')    # Clears the screen

        showQuizLogo()
        print("Your current score: " + str(score) + " / " + str(max_num_questions) + "\n")
        

    print("\n\n********************************************************************************")         
    print("You've finished the quiz. You got " + str(score) + " out of " + str(max_num_questions) + "!")

    score_percentage = 100 * float(score)/float(max_num_questions)

    if score_percentage >= 90:
        print("Right on, " + name + "! You definitely know your Python :)")
    elif score_percentage < 90 and score_percentage > 50:
        print("You did actually pretty well, " + name + ". Good job!")
    else:
        print("Oh, you might need to study more about Python, " + name +". Maybe have it a go again?")

    print("********************************************************************************")


# Start with the main() function     
if __name__ == "__main__":
    main()
