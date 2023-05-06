import java.util.Scanner;
import java.util.Random;

class GuessNumber{
    int myNumber, number, attempt = 0;
    // constructor to generate a random number
    public GuessNumber(){
        System.out.println("Guess the number between 1 to 100");
        Random rand = new Random();
        // Generating a random integer between 1 to 100
        number = 1 + rand.nextInt(100);
    }
    Scanner sc = new Scanner(System.in);
    // userInput method to take user input
    void userInput(){
        myNumber = sc.nextInt();
    }
    // guess method to check that given number is equal to random number or not
    public void guess(){
        while (myNumber != number){
            userInput();
            attempt++;
            if (myNumber > number){
                System.out.println("Please enter a smaller number!");
            }
            else if (myNumber < number) {
                System.out.println("Please enter a greater number!");
            }
            else {
                System.out.println("You guessed the number in "+  attempt+ " attempts");
            }
        }
    }
}

public class GuessTheNumber {
    public static void main(String[] args) {
        GuessNumber myGuesses = new GuessNumber();
        myGuesses.guess();
    }
}
