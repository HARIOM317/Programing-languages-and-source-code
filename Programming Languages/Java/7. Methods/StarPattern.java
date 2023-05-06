public class StarPattern {
    static void starPattern(int n){
        for (int i = 1; i <= n; i++){
            for (int j = 1; j <= i; j++){
                System.out.print("* ");
            }
            System.out.print("\n");
        }
    }
    public static void main(String[] args) {
        starPattern(5);
    }
}
