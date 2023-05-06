import java.util.Scanner;

public class NestedTryCatch {
    public static void main(String[] args) {
        int [] arr = {10, 20, 30, 40, 50};
        Scanner sc = new Scanner(System.in);

        try {
            while (true){
                System.out.print("Enter array index : ");
                int index = sc.nextInt();
                System.out.println("The value at index "+index+" is : "+arr[index]);

                // nested try-catch block
                try{
                    System.out.print("Enter number to divide given index : ");
                    int no = sc.nextInt();
                    System.out.println("Answer : "+arr[index]/no);
                }
                catch (Exception e){
                    System.out.println("Exception in level 2");
                    System.out.println("Can not divided by zero!");
                }
            }
        }
        catch (Exception e){
            System.out.println("Exception in level 1");
            System.out.println("Index does not exist!");
        }
    }
}
