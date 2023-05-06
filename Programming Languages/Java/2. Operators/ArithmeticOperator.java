public class ArithmeticOperator {
    public static void main(String[] args) {
        float a = 8;
        float b = 5;
        // Arithmetic operators (+, -, *, /, %, ++, --)
        float sum = a+b;
        float sub = a-b;
        float mul = a*b;
        float div = a/b;
        float rem = a%b;

        System.out.println("a = "+a);
        System.out.println("b = "+b);
        System.out.println("sum = "+sum);
        System.out.println("sub = "+sub);
        System.out.println("mul = "+mul);
        System.out.println("div = "+div);
        System.out.println("rem = "+rem);

        a++;
        b--;
        System.out.println("a++ = "+a);
        System.out.println("b-- = "+b);
    }
}
