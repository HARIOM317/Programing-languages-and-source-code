class X{
    X (){
        System.out.println("This is default constructor of class X");
    }

    void sayHello(String name){
        System.out.println("Hello, "+name);
    }
}
class Y extends  X{
    Y (){
        System.out.println("This is default constructor of class Y");
    }
}
class Z extends Y{
    Z (){
        System.out.println("This is default constructor of class Z");
    }
}

public class MultilevelInheritance {
    public static void main(String[] args) {
        Z z1 = new Z();     // X -> Y -> Z
        z1.sayHello("Hariom");
    }
}
