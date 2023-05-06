import java.util.Scanner;
public class SwitchStatement {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter 1 if your age is less than 18\nEnter 2 if your age is more than or equal to 18 and less than 30\nEnter 3 if your age is more than or equal to 30 and less than 60\nEnter 4 if your age is more than 60");
        byte age = sc.nextByte();

        // Normal switch statement
        switch (age){
            case 1:
                System.out.println("You are not eligible!");
                break;
            case 2:
                System.out.println("You are eligible!");
                break;
            case 3:
                System.out.println("You are experienced!");
                break;
            case 4:
                System.out.println("You are retired!");
                break;
            default:
                System.out.println("Invalid choice!");
                break;
        }

        // Enhanced switch statement
        /*
        switch (age) {
            case 1 -> System.out.println("You are not eligible!");
            case 2 -> System.out.println("You are eligible!");
            case 3 -> System.out.println("You are experienced!");
            case 4 -> System.out.println("You are retired!");
            default -> System.out.println("Invalid choice!");
        }
        */
    }
}
