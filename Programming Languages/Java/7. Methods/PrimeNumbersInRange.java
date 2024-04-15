public class PrimeNumbersInRange {
    // Helper Function to check that a number is prime or not
    public static boolean isPrime(int n){
        if(n==2){
            return true;
        }
        for(int i = 2; i <= Math.sqrt(n); i++){
            if(n%i == 0){
                return false;
            }
        }
        return true;
    }

    public static void primeInRange(int n1, int n2){
        for(int i = n1; i <= n2; i++){
            if(isPrime(i)){
                System.out.print(i+" ");
            }
        }
    }

    public static void main(String[] args) {
        int n1 = 1, n2 = 500;
        primeInRange(n1, n2);
    }
}
