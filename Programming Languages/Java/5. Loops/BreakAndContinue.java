public class BreakAndContinue {
    public static void main(String[] args) {
        int i;
        for (i = 1; i < 100; i++){
            if (i%3==0){
                continue;   // skip multiples of 3
            }
            if (i>60){
                break;    // exit from loop when i > 60
            }
            System.out.print(i+" ");
        }
    }
}
