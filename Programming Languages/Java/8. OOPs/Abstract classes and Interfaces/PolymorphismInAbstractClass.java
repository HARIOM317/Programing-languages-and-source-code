abstract class Telephone{
    abstract void ring();
    abstract void lift();
    abstract void disconnect();
}

class NewPhone extends Telephone{
    void ring(){
        System.out.println("Ringing...");
    }
    void lift(){
        System.out.println("Lifting...");
    }
    void disconnect(){
        System.out.println("Disconnecting...");
    }
    void call(){
        System.out.println("Calling...");
    }
}

public class PolymorphismInAbstractClass {
    public static void main(String[] args) {
        Telephone t1 = new NewPhone();
        t1.ring();
        t1.lift();
        t1.disconnect();
        // t1.call(); --> Not allowed
    }
}
