class C1{
    public int x = 5;
    protected int y = 45;
    int z = 10;
    private int a = 50;

    // we can access all properties(public, private, protected, default) in same class
    public void meth1(){
        System.out.println("x = "+x);
        System.out.println("y = "+y);
        System.out.println("z = "+z);
        System.out.println("a = "+a);
    }
}

class C2 extends C1{
    C2(){
        System.out.println("value of x = "+x);  // accessible
        System.out.println("value of y = "+y);  // accessible
        System.out.println("value of z = "+z);  // accessible
       // System.out.println("\nvalue of a = "+a);  // not accessible
    }
}

public class AccessModifiers {
    public static void main(String[] args) {
        System.out.println("\nAccess specifier inside same class");
        C1 c1 = new C1();
        c1.meth1();     // accessible all access modifiers in same class

        System.out.println("\nAccess specifier inside same package");
        // System.out.println(c1.a);   // not accessible private properties of class in same package
        System.out.println(c1.x);   // accessible
        System.out.println(c1.y);   // accessible
        System.out.println(c1.z);   // accessible

        System.out.println("\nAccess specifier inside sub class");
        C2 c2 = new C2();   // use class1 property by class 2 (accessible only - public, default and protected)
    }
}
