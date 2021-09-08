from ast import Num
import random
import time
import copy

def number_guessing_game(NumberOfGuesses):
    """
    A simple number guessing game where the computer picks a number 
    and the user has to guess it.
    Loops over for as long as the user wants to play.

    Parameters:
        NumberOfGuesses = Stores the number of guesses the user has.
                          Is used to reset the amount if the olayer 
                          wants to play again.
    
    Variables:
        number_of_guesses = Stores the number of guesses the user has.
        
        computer_choice = Stores the number the computer chooses.
        
        user_guess = Stores the user's guess.

        play_again = Stores whether the user wants to play again 
                     or not.
    """
    number_of_guesses = copy.deepcopy(NumberOfGuesses)
    computer_choice = None
    user_guess = None
    play_again = "yes"

    print("We are going to play a guessing game.")
    while play_again == "yes":
        number_of_guesses = copy.deepcopy(NumberOfGuesses)
        time.sleep(1)
        print(f"I have picked a number between 1-100, and you have to guess what it is within {NumberOfGuesses} tries")
        computer_choice = random.randint(1,100)

        while number_of_guesses > 0 :
            user_guess = get_valid_number_from_user()
            number_of_guesses -= 1
            if user_guess > computer_choice:
                print("That's too high.")
            elif user_guess < computer_choice:
                print("That's too low.")
            elif user_guess == computer_choice:
                print("Wow you got it right!")
                time.sleep(2)
                print(f"You had {number_of_guesses} guesses remaining.")
                break
            if number_of_guesses == 0:
                print("Oops, you've had too many guesses, which means you lose!")
                time.sleep(2)
                print(f"The right answer was {computer_choice}.")
        
        play_again = input("Would you like to play again? \n(yes/no) \n")
    print("Thank you for playing!")



def get_valid_number_from_user():
    """
    This method makes sure the user provides a valid number 
    as an input.

    Variables:
        valid_response = Checks to see if the user has entered a 
                         valid response.
        
        user_guess = Stores the user's guess.
    """
    valid_response = False
    while valid_response == False:
        try:
            user_guess = int(input("What is your guess? \n"))
            valid_response = True
        except:
            print("Invalid input, try again.")
    return user_guess



if __name__ == "__main__":
    number_guessing_game(NumberOfGuesses = 5)