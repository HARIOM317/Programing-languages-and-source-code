public class LogicalOperator {
    public static void main(String[] args) {
        float a = 8;
        float b = 5;
        // Comparison operators (&&, ||, !)
        System.out.println("a = "+a);
        System.out.println("b = "+b);

        System.out.println("!(a==b) : "+ !(a==b));
        System.out.println("a>=b && a<10 : "+ (a>=b && a<10));
        System.out.println("a>b || a==5 : "+ (a>b || a==5));
    }
}
