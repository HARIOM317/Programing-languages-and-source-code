public class StaticMethod {
    static void collageName(){
        System.out.println("My collage name is SISTec");
    }
    public void branch(){
        System.out.println("My branch is CSE");
    }

    public static void main(String[] args) {
        collageName();  // We can call static method without creating object of this class
        StaticMethod s1 = new StaticMethod();
        s1.branch();    // We need to create an object to call this non-static method
    }
}
