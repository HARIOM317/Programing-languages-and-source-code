class A{
    public int x, y;
    public String name;
    public float salary;

    A(){
        System.out.println("This is the constructor of class A (Base)");
    }

    A(String name, float salary){
        this.name = name;
        this.salary = salary;
    }

    A(int a){
        System.out.println("I am an overloaded constructor of class A with value of a as : "+a);
    }

    A(float a){
        System.out.println("Base class constructor with value of float a = "+a);
    }
    public void display(){
        System.out.println("Name = "+name);
        System.out.println("Salary = "+salary);
    }
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
}

class B extends A{
    public int y;
    public int z;

    B(){
        super(20);      // this will run the constructor of base class which take an argument int
        System.out.println("This is the constructor of class B (Derived)");
        this.x = 5;
        this.y = 10;
        this.z = 15;
    }

    B(int a){
        System.out.println("This is the constructor of class B (Derived)");
    }

    B(float a, float b){
        super(a);   // call it's base class constructor which take 1 float argument
        System.out.println("Derived class constructor with value of float b = "+b);
    }
    public void get(){
        System.out.println("x = "+x);
        System.out.println("y = "+y);
        System.out.println("z = "+z);
    }
}

class C extends B{
    C(){
        System.out.println("This is constructor of child class C");
    }

    C(float a, float b, float c){
        super(a, b);    // call it's base class constructor which take 2 float arguments
        System.out.println("Child class constructor with value of float c = "+c);
    }
}

public class ConstructorInInheritance {
    public static void main(String[] args) {
        B b1, b2;

        System.out.println("\nFor object b1");
        b1 = new B(5);
        b1.setX(100);
        b1.setY(200);
        System.out.println("X = "+b1.getX());
        System.out.println("Y = "+b1.getY());

        System.out.println("\nFor object b2");
        b2 = new B();
        b2.get();

        System.out.println("\nFor object a");
        A a = new A("Hariom", 20202020.2020f);
        a.display();

        System.out.println("\nFor object c");
        C c = new C(10.0f, 20.0f, 30.0f);   // this will call constructor which takes three float arguments
    }
}
