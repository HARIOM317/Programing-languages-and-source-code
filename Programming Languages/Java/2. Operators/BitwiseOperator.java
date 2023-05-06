public class BitwiseOperator {
    public static void main(String[] args) {
        int a = 5;
        int b = 7;
        System.out.println("a = "+a);
        System.out.println("b = "+b);

        // Bitwise operators [ &(bitwise and), |(bitwise or), ^(bitwise xor), ~(bitwise complement) ]

        // bitwise and
        // 0101 & 0111 = 0101 = 5
        System.out.println("a&b : "+ (a&b));
        // bitwise or
        // 0101 | 0111 = 0111 = 7
        System.out.println("a|b : "+ (a|b));
        // bitwise xor
        // 0101 ^ 0111 = 0010 = 2
        System.out.println("a^b : "+ (a^b));
        // bitwise complement
        System.out.println("~a : "+ (~a));
    }
}
