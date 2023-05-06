import java.util.Scanner;
public class IfElse {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your age : ");
        byte age = sc.nextByte();

        // If - else
        if (age >= 18){
            System.out.println("You can vote!");
        }
        else {
            System.out.println("You can not vote!");
        }
    }
}
