@FunctionalInterface
interface MyFunctionalInterface{
    void myName();  // Can declare only one method because this interface in functional
}

class Base{
    public void greet(String name){
        System.out.println("Good Morning, "+ name);
    }
}

class Derived extends Base{
    @Override
    public void greet(String name){
        System.out.println("Hello, "+ name);
    }

    @Deprecated
    public int sum(int a , int b){
        return a+b;
    }

    @SuppressWarnings("deprecation")
    void noWarning(){
        Derived d1 = new Derived();
        System.out.println("Sum = "+ d1.sum(40, 50));   // no warning because of deprecation notation
    }
}

public class Notations {
    public static void main(String[] args) {
        Derived d = new Derived();
        d.greet("Hariom");
        int addition = d.sum(10, 20);      // because of deprecated notation
        System.out.println(addition);
        d.noWarning();
    }
}
