public class AssociativityOfOperators {
    public static void main(String[] args) {
        // Precedence and Associativity

        // Precedence of * = Precedence of / (Associativity left - right)
        // Precedence of + = Precedence of - (Associativity left - right)
        int a = 6*3/2+5-4;   // 18/2+1 = 9+1 = 10
        int b = 6/3*2-5+4;   // 2*2-1 = 4-1 = 3
        int c = 5;
        int d = 5*++c;  // 5*6 = 30
        float e = 7/4 * 9/3;    // 1*9/3 = 9/3 = 3.0
        float f = 7/4.0f * 9/3;     // 1.75*9/3 = 15.75/3 = 5.25
        float g = 7/4.0f * 7/4.0f;      // 1.75*7/4.0 = 12.25/4.0 = 3.0625
        float h = 7/4 * 7/4.0f;     // 1*7/4.0 = 7/4.0 = 1.75
        System.out.println(a);
        System.out.println(b);
        System.out.println(d);
        System.out.println(e);
        System.out.println(f);
        System.out.println(g);
        System.out.println(h);
    }
}