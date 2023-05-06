public class Recursion {
    static int sumOfN(int n){
        if (n==0 || n==1){
            return n;
        }
        // recursion
        return n + sumOfN(n-1);
    }
    public static void main(String[] args) {
        int n = 6;
        System.out.println("Sum of first "+n+" natural number is : "+ sumOfN(n));
    }
}
