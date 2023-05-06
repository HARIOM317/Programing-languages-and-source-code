import java.util.Scanner;
public class MultiDimensionalArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        byte n, m;
        System.out.print("Enter row : ");
        n = sc.nextByte();
        System.out.print("Enter columns : ");
        m = sc.nextByte();

        // creating matrix
        int[][] matrix1 = new int[n][m];
        int[][] matrix2 = new int[n][m];
        int[][] sum = new int[n][m];

        // input elements of matrix 1
        System.out.println("Enter elements of matrix 1");
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                matrix1[i][j] = sc.nextInt();
            }
        }
        // input elements of matrix 2
        System.out.println("Enter elements of matrix 2");
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                matrix2[i][j] = sc.nextInt();
            }
        }
        // adding matrix1 and matrix2
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                sum[i][j] = matrix1[i][j] + matrix2[i][j];
            }
        }
        // output sum of matrix1 and matrix2
        System.out.println("Sum of matrix1 and matrix 2 is :");
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                System.out.print(sum[i][j]+" ");
            }
            System.out.print("\n");
        }
    }
}
