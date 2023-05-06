public class AssignmentOperator {
    public static void main(String[] args) {
        float a = 8;
        float b = 5;
        float c = 2;
        // Assignment operators (=, +=, -=, *=, /=, %=)
        System.out.println("a = "+ a);
        System.out.println("b = "+ b);
        System.out.println("c = "+ c);
        System.out.println("a+=b = "+ (a+=b));
        System.out.println("b-=c = "+ (b-=c));
        System.out.println("c*=5 = "+ (c*=5));
        System.out.println("a/=3 = "+ (a/=3));
        System.out.println("b%=8 = "+ (b%=8));
        System.out.println("a=8 =  "+ (a=8));
    }
}
