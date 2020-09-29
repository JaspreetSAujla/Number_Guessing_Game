import java.util.Scanner;
import java.util.Random;

class NumberGame {
    public static void main(String[] args) {
        System.out.println("We are going to play a guessing game.");
        System.out.println("I have picked a number between 0-100, and you have to guess what it is within 5 tries");
        Random NumObject = new Random();
        int number = NumObject.nextInt(101);
        int num_of_guesses = 0;
        Scanner scn = new Scanner(System.in);
        while (num_of_guesses < 5) {
            System.out.println("What is your guess?");
            int guess = scn.nextInt();
            num_of_guesses += 1;
            if (guess > number) {
                System.out.println("That's too high.");
            } else if (guess < number) {
                System.out.println("That's too low.");
            } else {
                System.out.println("Wow you guessed it right in " + Integer.toString(num_of_guesses) + " tries.");

            }
        }
        scn.close();
        System.out.println("Oops, you have had too many tries.");
        System.out.println("The number was " + Integer.toString(number) + ".");
    }
}