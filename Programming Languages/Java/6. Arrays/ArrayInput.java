import java.util.Scanner;
public class ArrayInput {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int [] arr = new int[5];
        // Input array elements
        System.out.println("Enter array's element");
        for (int i = 0; i < arr.length; i++){
            arr[i] = sc.nextInt();
        }

        // Output array elements
        System.out.println("Array's element are");
        for (int i = 0; i < arr.length; i++){
            System.out.print(arr[i]+" ");
        }
    }
}
