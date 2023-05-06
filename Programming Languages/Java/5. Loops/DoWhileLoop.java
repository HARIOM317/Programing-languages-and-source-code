public class DoWhileLoop {
    public static void main(String[] args) {
        int a = 10;
        // do-while loop always runs at least one time even condition is false
        do {
            System.out.println("The do-while loop has been executed successfully!");
            a++;    // increment value of a
        }while (a < 5);     // condition
        System.out.println("a = "+a);
    }
}
