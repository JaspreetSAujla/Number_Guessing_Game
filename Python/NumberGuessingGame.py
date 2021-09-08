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
        question_1 = Stores the first question.

        question_2 = Stores the second question.

        computer_choice = Stores the number the computer chooses.
        
        user_guess = Stores the user's guess.

        play_again = Stores whether the user wants to play again 
                     or not.
    """
    question_1 = "What is your guess? \n"
    question_2 = "How many guesses do you want for the next turn? \n"
    computer_choice = None
    user_guess = None
    play_again = "yes"

    print("We are going to play a guessing game.")
    while play_again == "yes":
        time.sleep(1)
        print(f"I have picked a number between 1-100, and you have to guess what it is within {NumberOfGuesses} tries")
        computer_choice = random.randint(1,100)

        while NumberOfGuesses > 0 :
            user_guess = get_valid_response(Question = question_1)
            NumberOfGuesses -= 1
            if user_guess > computer_choice:
                print("That's too high.")
            elif user_guess < computer_choice:
                print("That's too low.")
            elif user_guess == computer_choice:
                print("Wow you got it right!")
                time.sleep(2)
                print(f"You had {NumberOfGuesses} guesses remaining.")
                break
            if NumberOfGuesses == 0:
                print("Oops, you've had too many guesses, which means you lose!")
                time.sleep(2)
                print(f"The right answer was {computer_choice}.")
        
        play_again = input("Would you like to play again? \n(yes/no) \n")
        if play_again == "yes":
            NumberOfGuesses = get_valid_response(Question = question_2)
    print("Thank you for playing!")



def get_valid_response(Question):
    """
    This method makes sure the user provides a valid input.

    Parameters:
        Question = Passes in the question asked to the user.

    Variables:
        valid_response = Checks to see if the user has entered a 
                         valid response.
        
        user_response = Stores the user's response.
    """
    valid_response = False
    while valid_response == False:
        try:
            user_response = int(input(Question))
            valid_response = True
        except:
            print("Invalid input, try again.")
    return user_response



if __name__ == "__main__":
    number_guessing_game(NumberOfGuesses = 5)