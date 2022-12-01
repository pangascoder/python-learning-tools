import datetime
import time
import os

from Person import Person

global user


def main():
  startFortuneTelling()

  # Ask if they want to try again
  try_again = input("\nWould you like to try again? [y/n]: ")

  while try_again == "y" or try_again == "yes":
      os.system('cls')    # Clears the screen
      startFortuneTelling()  
      try_again = ""      # Clear the previous input
      try_again = input("\nWould you like to try again? [y/n]: ")

def getUserInfo():
  global user

  name = input("What is your name? ")
  birthyear = input("What year were you born? ")
  birthmonth = input("Which month were you born? ")
  birthdate = input("What day were you born? (Please give a number): ")

  # Convert month to equivalent number
  birthmonth = datetime.datetime.strptime(birthmonth, '%B').month

  user = Person(name, birthyear, birthmonth, birthdate)


def startFortuneTelling():
  os.system('cls')
  displayAppLogo()
  print("\n\n")
  # Get user information and then display
  getUserInfo()
  displayUserInfo()

  # Ask user if they want their fortune told
  input_valid = False

  while input_valid == False:
    user_choice = input("Would you like your fortune told? [Y/N] ")
    if user_choice.lower() == "y":
      input_valid = True
      print("Beware...")
      time.sleep(1)
      print("Your future awaits...")
      time.sleep(1)
      print("*******************")
      print(user.fortune)
      print("*******************")
      time.sleep(5)  # Delay before trying another fortune
    elif user_choice.lower() == "n":
      input_valid = True
      print("Farewell then...")
    else:  # Invalid input (neither Y or N)
      print("You didn't answer properly...")
      input_valid = False

def displayAppLogo():
  print(""" 
  
 
                        _  .-')   .-') _                    .-') _   ('-.         .-') _     ('-.                        ('-.  _  .-')   
                       ( \( -O ) (  OO) )                  ( OO ) )_(  OO)       (  OO) )  _(  OO)                     _(  OO)( \( -O )  
   ,------. .-'),-----. ,------. /     '._ ,--. ,--.   ,--./ ,--,'(,------.      /     '._(,------.,--.      ,--.     (,------.,------.  
('-| _.---'( OO'  .-.  '|   /`. '|'--...__)|  | |  |   |   \ |  |\ |  .---'      |'--...__)|  .---'|  |.-')  |  |.-')  |  .---'|   /`. ' 
(OO|(_\    /   |  | |  ||  /  | |'--.  .--'|  | | .-') |    \|  | )|  |          '--.  .--'|  |    |  | OO ) |  | OO ) |  |    |  /  | | 
/  |  '--. \_) |  |\|  ||  |_.' |   |  |   |  |_|( OO )|  .     |/(|  '--.          |  |  (|  '--. |  |`-' | |  |`-' |(|  '--. |  |_.' | 
\_)|  .--'   \ |  | |  ||  .  '.'   |  |   |  | | `-' /|  |\    |  |  .--'          |  |   |  .--'(|  '---.'(|  '---.' |  .--' |  .  '.' 
  \|  |_)     `'  '-'  '|  |\  \    |  |  ('  '-'(_.-' |  | \   |  |  `---.         |  |   |  `---.|      |  |      |  |  `---.|  |\  \  
   `--'         `-----' `--' '--'   `--'    `-----'    `--'  `--'  `------'         `--'   `------'`------'  `------'  `------'`--' '--' 
 
 
 
 """)


def displayUserInfo():
  global user

  print("\n\n")
  print("Thank you, " + user.name +", for providing your details.")
  time.sleep(2)
  print("According to what you've told me, you are currently " + str(user.age) + " years old.")
  time.sleep(3)
  print("Your zodiac sign is " + user.zodiac_sign.value + ".") 
  time.sleep(2)
  print("You were born in the year of the " + user.animal_year + ".")
  time.sleep(2)
  print("Your birthstone is " + user.birthstone + ".")
  time.sleep(2)
  print("And your element is " + user.element + ".")
  print("\n\n")
  time.sleep(2)
  
# Start with the main() function
if __name__ == "__main__":
  main()
