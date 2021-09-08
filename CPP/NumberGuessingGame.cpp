#include<iostream>
#include<cstdlib>
#include<ctime>
using namespace std;

int randomNumber(int startNumber, int endNumber) {
    /*
    Takes a start number and an end number and picks 
    a random number between that range.
    endNumber is EXCLUSIVE, similar to python range function.
    */
    srand(time(0));
    int number = startNumber + (rand() % endNumber);
    return number;
}



int getValidResponse(string question) {
    /*
    This method makes sure the user provides a valid input.

    Parameters:
        question = Passes in the question asked to the user.

    Variables:
        validResponse = Checks to see if the user has entered a 
                        valid response.
        
        userResponseString = Stores the string response which is 
                             turned into an int.
            
        userResponse = Stores the user's response.
    */
    bool validResponse = false;
    string userResponseString;
    int userResponse;
    while (validResponse == false) {
        try {
            cout << question;
            cin >> userResponseString;
            userResponse = stoi(userResponseString);
            return userResponse;
        } catch(const exception e) {
            cout << "Invalid input, try again. \n";
        }
    }
    return 10;
}



void numberGuessingGame(int numberOfGuesses) {
    /*
    A simple number guessing game where the computer picks a number 
    and the user has to guess it.
    Loops over for as long as the user wants to play.

    Parameters:
        numberOfGuesses = Stores the number of guesses the user has.
                          Is used to reset the amount if the olayer 
                          wants to play again.
        
    Variables:
        question_1 = Stores the first question.

        question_2 = Stores the second question.
            
        computerChoice = Stores the number the computer chooses.
            
        userGuess = Stores the user's guess.

        playAgain = Stores whether the user wants to play again 
                    or not.
    */
    string question_1 = "What is your guess? \n";
    string question_2 = "How many guesses would you like for your next game? \n";
    int computerChoice;
    int userGuess;
    string playAgain = "yes";

    cout << "We are going to play a number guessing game. \n";
    while (playAgain == "yes") {
        cout << "I have picked a number between 1-100, and you have to guess what it is within " << numberOfGuesses << " tries. \n";
        computerChoice = randomNumber(1, 101);

        while (numberOfGuesses > 0) {
            userGuess = getValidResponse(question_1);
            numberOfGuesses -= 1;
            if (userGuess > computerChoice) {
                cout << "That's too high. \n";
            } else if (userGuess < computerChoice) {
                cout << "That's too low. \n";
            } else {
                cout << "You got it right! \n";
                cout << "You had " << numberOfGuesses << " guesses remaining. \n";
                break;
            }
            if (numberOfGuesses == 0) {
                cout << "Oops! You have had too many guesses, which means you lose. \n";
                cout << "The correct answer was " << computerChoice << ". \n";
            }
        }
        cout << "Would you like to play again? \n(yes/no) \n";
        cin >> playAgain;
        if (playAgain == "yes") {
            numberOfGuesses = getValidResponse(question_2);
        }
    }
    cout << "Thank you for playing! \n";
}



int main() {
    numberGuessingGame(7);
    return 0;
}