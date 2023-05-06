// creating interface that has four methods
interface A{
    // method are by default public and abstract
    void a();
    void b();
    void c();
    void d();
}

// creating abstract class that provides the implementation of one method of A interface
abstract class B implements A{
    public void c(){
        System.out.println("I am method c");
    }
}

// creating subclass of abstract class, now we need to provide the implementation of rest of the methods
class M extends B{
    public void a(){
        System.out.println("I am a");
    }
    public void b(){
        System.out.println("I am b");
    }
    public void d(){
        System.out.println("I am d");
    }
}

public class AbstractClassAndInterface {
    public static void main(String[] args) {
        A a = new M();
        a.a();
        a.b();
        a.c();
        a.d();
    }
}
