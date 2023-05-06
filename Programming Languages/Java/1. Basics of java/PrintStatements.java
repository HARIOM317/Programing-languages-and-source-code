public class PrintStatements {
    public static void main(String[] args) {
        int a = 6;
        float b = 5.268768f;
        System.out.println("a = "+a);       // add new line
        System.out.print("b = "+b);     // no line added
        System.out.printf("\na = %d and b = %.2f", a, b);     // print value using access specifier
        System.out.format("\na = %d and b = %10.3f", a, b);   // add 5 more white spaces (use 10 spaces) before value of b and print only three decimal value because of %10.3f
    }
}
