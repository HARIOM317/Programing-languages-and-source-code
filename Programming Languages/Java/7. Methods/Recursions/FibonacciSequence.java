import java.util.Scanner;
public class FibonacciSequence {
    static int fibonacci(int n){
        if (n==1 || n==2){
            return n-1;
        }
        // recursion
        return fibonacci(n-1)+fibonacci(n-2);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n : ");
        int n = sc.nextInt();
        System.out.println("The "+n+"th element of fibonacci series is : "+fibonacci(n));
    }
}
