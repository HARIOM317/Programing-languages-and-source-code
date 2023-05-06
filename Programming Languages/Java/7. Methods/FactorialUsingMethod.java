import java.util.Scanner;
public class FactorialUsingMethod {
    // method for finding factorial of a number
    static int factorial(int num){
        int fact = 1;
        for (int i = 1; i <= num; i++){
            fact *= i;
        }
        return fact;
    }

    // main method
    public static void main(String[] args) {
        Scanner mySc = new Scanner(System.in);
        System.out.print("Enter a number for factorial : ");
        int n = mySc.nextInt();
        System.out.println("Factorial = "+ factorial(n));
    }
}
