class Base{
    public Base(){
        System.out.println("This is the constructor of Base class");
    }
}

// inherit Base class in Derived class
class Derived extends Base{
    public Derived(){
        System.out.println("This is the constructor of Derived class");
    }
}

public class SingleInheritance {
    public static void main(String[] args) {
        Derived d = new Derived();
    }
}
