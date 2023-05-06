/* abstract class - abstract class is the class with whose help we create other classes

We can not make object of abstract class because it is a standard to make a class for other classes
 */

// abstract class
abstract class Greeting{
    Greeting (){
        System.out.println("This is the constructor of Greeting class!");
    }

    public void sayHello(String name){
        System.out.println("Hello, "+name);
    }

    // abstract method
    // Note : Either we can implement abstract method in it's derived class, or we can make it's derived class abstract.
    // we can implement these methods in it's derived class, and we can override theme according to our need in all derived classes.
    abstract void greet(String name);
    abstract void timeDuration();
    // Note : It is necessary to implement all the abstract methods of base class in it's derived class if we don't make them abstract
}

// concrete class
class Morning extends Greeting{
    // abstract method implementation
    @Override
    public void greet(String name){
        System.out.println("\nGood morning, "+name);
    }

    @Override
    void timeDuration(){
        System.out.println("6:00 AM to 11:59 AM");
    }
}

// concrete class
class AfterNoon extends Greeting{
    // abstract method implementation
    public void greet(String name){
        System.out.println("\nGood afternoon, "+name);
    }

    void timeDuration(){
        System.out.println("12:00 AM to 04:59 PM");
    }
}

// concrete class
class Evening extends Greeting{
    // abstract method implementation
    public void greet(String name){
        System.out.println("\nGood evening, "+name);
    }

    void timeDuration(){
        System.out.println("5:00 PM to until we do not sleep");
    }
}

// abstract class
abstract class Night extends Greeting{
    void sleep(){
        System.out.println("Good night!");
    }
}

public class AbstractClasses {
    public static void main(String[] args) {
        // Greeting g = new Greeting();     // Not valid
        // Night n = new Night();     // Not valid

        Morning m = new Morning();
        AfterNoon a = new AfterNoon();
        Evening e = new Evening();

        m.greet("Hariom");
        m.timeDuration();
        m.sayHello("HSR");

        a.greet("Abhishek");
        a.timeDuration();
        a.sayHello("Abhi");

        e.greet("Aman");
        e.timeDuration();
        e.sayHello("Aman");

    }
}
