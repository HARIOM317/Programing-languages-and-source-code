import java.util.Scanner;

public class UserInput {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Taking complete string as input
        System.out.println("Enter a sentence : ");
        String sentence = input.nextLine();
        System.out.println("Your sentence is : "+sentence);

        // Taking string as input (Only one word/ignore after space)
        System.out.print("Enter a word : ");
        String str = input.next();
        System.out.println("Your word is : "+str);

        // area of circle
        System.out.println("Enter radius for circle: ");
        int r = input.nextInt();
        float pi = 3.14f;
        System.out.println("Area of Circle = "+(pi*r*r));

//        boolean check = input.hasNextInt();
//        Check that given number is integer or not
//        System.out.println("Radius is integer = "+check);
    }
}
