import java.util.Scanner;
import java.util.Random;

public class RockPaperScissor {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random rand = new Random();

        // Generating a random integer between 1 to 3
        int computerChoice = 1 + rand.nextInt(3);

        System.out.println("Welcome in Rock-Paper-Scissor Game");
        System.out.println("Follow the given instructions to play this game");
        System.out.println("\n\tEnter 1 to choose Rock\n\tEnter 2 to choose Paper\n\tEnter 3 to choose Scissor\n");

        System.out.print("Choice : ");
        int userChoice = sc.nextInt();

        if (computerChoice == 1 && userChoice == 1){
            System.out.println("\nComputer chooses : Rock\nUser chooses : Rock");
            System.out.println("Match draw!");
        }
        else if (computerChoice == 1 && userChoice == 2){
            System.out.println("\nComputer chooses : Rock\nUser chooses : Paper");
            System.out.println("You won!");
        }
        else if (computerChoice == 1 && userChoice == 3){
            System.out.println("\nComputer chooses : Rock\nUser chooses : Scissor");
            System.out.println("You lose!");
        }
        else if (computerChoice == 2 && userChoice == 1){
            System.out.println("\nComputer chooses : Paper\nUser chooses : Rock");
            System.out.println("You lose!");
        }
        else if (computerChoice == 2 && userChoice == 2){
            System.out.println("\nComputer chooses : Paper\nUser chooses : Paper");
            System.out.println("Match draw!");
        }
        else if (computerChoice == 2 && userChoice == 3){
            System.out.println("\nComputer chooses : Paper\nUser chooses : Scissor");
            System.out.println("You won!");
        }
        else if (computerChoice == 3 && userChoice == 1){
            System.out.println("\nComputer chooses : Scissor\nUser chooses : Rock");
            System.out.println("You won!");
        }
        else if (computerChoice == 3 && userChoice == 2){
            System.out.println("\nComputer chooses : Scissor\nUser chooses : Paper");
            System.out.println("You lose!");
        }
        else if (computerChoice == 3 && userChoice == 3){
            System.out.println("\nComputer chooses : Scissor\nUser chooses : Scissor");
            System.out.println("Match draw!");
        }
        else {
            System.out.println("Invalid choice");
        }
    }
}
