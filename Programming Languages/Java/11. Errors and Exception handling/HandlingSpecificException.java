import java.util.Scanner;

public class HandlingSpecificException {
    public static void main(String[] args) {
        int [] marks = {76, 98, 46, 86, 95, 100, 85, 97};
        Scanner sc = new Scanner(System.in);

        try {
            System.out.print("Enter the array index : ");
            int index = sc.nextInt();
            System.out.println("The value at index "+index+" is "+marks[index]);

            System.out.print("\nEnter the number you want to divide the value with : ");
            int divValue = sc.nextInt();
            System.out.println("Answer = "+marks[index]/divValue);
        }
        catch (ArrayIndexOutOfBoundsException e){
            System.out.println("ArrayIndexOutOfBoundsException occurred");
        }
        catch (ArithmeticException e){
            System.out.println("ArithmeticException occurred");
        }
        catch (Exception e){
            System.out.println("Some other Exception occurred");
        }
    }
}
