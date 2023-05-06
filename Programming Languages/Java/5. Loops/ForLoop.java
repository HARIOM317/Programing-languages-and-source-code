import java.util.Scanner;
public class ForLoop {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter starting number : ");
        int start = sc.nextInt();
        System.out.println("Enter ending number : ");
        int end = sc.nextInt();

        System.out.printf("Prime number between %d to %d \n", start, end);

        // for loop
        for (int i = start; i <= end; i++){
            int j;
            for (j = 2; j < i; j++){
                if (i%j == 0){
                    break;
                }
            }
            if (i == j){
                System.out.print(i+" ");
            }
        }
    }
}
