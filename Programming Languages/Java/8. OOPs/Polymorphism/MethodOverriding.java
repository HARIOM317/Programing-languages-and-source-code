// base class
class A{
    public int a;
    public void display(){
        System.out.println("I am display method of class A");
    }

    public void sum(int a, int b){
        System.out.println("Sum = "+ (a+b));
    }
}

// derived class
class B extends A{
    // method overriding without override notation
    public void display(){
        System.out.println("I am display method of class B");
    }

    // method overriding with @Override notation
    @Override       // override notation to indicate that following method is overriding and if method is not overriding than it will throw an error because of override notation
    public void sum(int a, int b){
        System.out.println("Addition = "+ (a+b));
    }
}

public class MethodOverriding {
    public static void main(String[] args) {
        B b = new B();
        b.display();
        b.sum(10, 45);
    }
}
