package Java;

import java.util.Scanner;
import java.util.Random;

class NumberGuessingGame {

    public static void numberGuessingGame(int numberOfGuesses) {
        /**
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
            
            scn = Stores the scanner.

            randomNumber = Picks a random number.
        */
        String question_1 = "What is your guess?";
        String question_2 = "How many guesses would you like for your next game?";
        int computerChoice;
        int userGuess;
        String playAgain = "yes";
        Scanner scn = new Scanner(System.in);
        Random randomNumber = new Random();

        System.out.println("We are going to play a number guessing game.");
        while (playAgain.equals("yes")) {
            System.out.println("I have picked a number between 1-100, and you have to guess what it is within " +
                                Integer.toString(numberOfGuesses) + " tries.");
            computerChoice = 1 + randomNumber.nextInt(100);

            while (numberOfGuesses > 0) {
                userGuess = getValidResponse(scn, question_1);
                numberOfGuesses -= 1;
                if (userGuess > computerChoice) {
                    System.out.println("That's too high.");
                } else if (userGuess < computerChoice) {
                    System.out.println("That's too low.");
                } else {
                    System.out.println("You got it right!");
                    System.out.println("Wow you had " + 
                                        Integer.toString(numberOfGuesses) + 
                                        " guesses remaining.");
                    break;
                }
                if (numberOfGuesses == 0) {
                    System.out.println("Oops, you've had too many guesses, which means you lose!");
                    System.out.println("The correct answer was " + Integer.toString(computerChoice));
                }
            }
            System.out.println("Would you like to play again? \r\n(yes/no)");
            playAgain = scn.nextLine();
            if (playAgain.equals("yes")) {
                numberOfGuesses = getValidResponse(scn, question_2);
            }
        }
        System.out.println("Thank you for playing!");
        scn.close();
    }



    private static int getValidResponse(Scanner scn, String question) {
        /**
        This method makes sure the user provides a valid input.

        Parameters:
            scn = Passes in the scanner.

            question = Passes in the question asked to the user.

        Variables:
            validResponse = Checks to see if the user has entered a 
                            valid response.
            
            userResponse = Stores the user's response.
        */
        Boolean validResponse = false;
        while (validResponse.equals(false)) {
            try {
                System.out.println(question);
                int userResponse = Integer.parseInt(scn.nextLine());
                return userResponse;
            } catch(Exception e) {
                System.out.println("Invalid input, try again.");
            }
        }
        // In case something breaks.
        return 10;
    }



    public static void main(String[] args) {
        numberGuessingGame(6);
    }
}