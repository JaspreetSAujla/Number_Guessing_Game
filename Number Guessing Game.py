import random
import time
import sys

if __name__ == "__main__":
    input("Press enter if the code does not continue")
    #Introduces script and computer picks a number.
    print("We are going to play a guessing game.")
    time.sleep(2)
    print("I have picked a number between 1-100, and you have to guess what it is within 5 tries")
    number = random.randint(1,100)
    num_of_guesses = 0
    #Loops over until either the player num_of_guesses or runs out of attempts.
    while num_of_guesses < 5:
        guess = int(input("What is your guess? \n"))
        num_of_guesses += 1
        if guess > number:
            print("That's too high.")
        elif guess < number:
            print("That's too low.")
        elif guess == number:
            print("Wow you got it right!")
            time.sleep(2)
            print("You guessed it in",num_of_guesses,"tries!")
            input("Press Enter and get out of here. \n")
            sys.exit()
    #Message if the player does not guess the number.
    print("Oops, you've had too many guesses, which means you lose!")
    time.sleep(2)
    print(f"The right answer was {number}.")
    input("Press enter to leave. \n")
    sys.exit()
