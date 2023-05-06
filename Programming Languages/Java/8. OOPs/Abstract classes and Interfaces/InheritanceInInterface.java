interface Base{
    void meth1();
    void meth2();
}

// Inheriting Base interface
interface Derived extends Base{
    void meth3();
    void meth4();
}

class Sample implements Derived{
    public void meth1(){
        System.out.println("This is method meth1 of Base interface");
    }
    public void meth2(){
        System.out.println("This is method meth2 of Base interface");
    }
    public void meth3(){
        System.out.println("This is method meth3 of Derived interface");
    }
    public void meth4(){
        System.out.println("This is method meth4 of Derived interface");
    }
}

public class InheritanceInInterface {
    public static void main(String[] args) {
        Sample s1 = new Sample();
        s1.meth1();
        s1.meth2();
        s1.meth3();
        s1.meth4();
    }
}
