import java.util.Scanner;

public class Errors {
    public static void main(String[] args) {
        /*
        There are three types of errors in java-
        1. Syntax error
        2. Logical error
        3. Runtime error -> (Also called Exception)
         */

        // 1. Syntax error
        // int a = 5  -> No semicolon, Syntax error

        // 2. Logical error
        System.out.print(2);        // logical error to print prime numbers
        for (int i = 1; i < 5; i++){
            System.out.print(" "+(2*i+1));
        }

        // 3. Runtime error
        System.out.print("\nEnter a number : ");
        Scanner sc = new Scanner(System.in);
        int i = sc.nextInt();
        System.out.println("Integer part of 1000 divided by "+i+" is : "+1000/i);   // Runtime error because 1000 can not divide by zero (0).
    }
}
