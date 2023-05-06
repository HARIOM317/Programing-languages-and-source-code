import java.util.Scanner;
public class DetectInteger {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number");
        boolean isInteger = sc.hasNextInt();

        if (isInteger){
            System.out.println("Given number is integer");
        }
        else {
            System.out.println("Given number is not integer");
        }
    }
}
