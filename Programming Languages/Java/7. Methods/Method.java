import java.util.Scanner;
public class Method {
    // non-static method
    int sum(int a, int b){
        return a+b;
    }

    // static method
    static int square(int n){
        return n*n;
    }

    // main method
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // creating an object of Method class
        Method obj = new Method();

        System.out.println("Enter first number");
        int a = sc.nextInt();
        System.out.println("Enter second number : ");
        int b  = sc.nextInt();

        // Calling non-static method by creating an object of the class
        System.out.println("Sum = "+ obj.sum(a, b));
        // calling method without using object because method is static
        System.out.println("Square of a = "+ square(a));
        System.out.println("Square of b = "+ square(b));
    }
}
