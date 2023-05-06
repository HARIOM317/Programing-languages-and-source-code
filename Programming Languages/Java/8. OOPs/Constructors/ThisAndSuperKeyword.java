class Animal{
    private String name, type;
    private boolean isDomestic, isDangerous;
    private String characteristic;

    Animal(){
        System.out.println("Hi, I am an Animal");
    }

    Animal (String type){
        this.type = type;
        System.out.println("Some animals can be dangerous and some are not but it is "+type+"\n");
    }

    public void setProperties(String name, boolean isDomestic, boolean isDangerous, String characteristic){
        this.name = name;
        this.isDomestic = isDomestic;
        this.isDangerous = isDangerous;
        this.characteristic = characteristic;
    }

    public void getProperties(){
        System.out.println("Animal Name : "+name);
        System.out.println("Is Domestic : "+isDomestic);
        System.out.println("Is Dangerous : "+isDangerous);
        System.out.println("Characteristics : "+characteristic+"\n");
    }
}

class Dog extends Animal{
    String type;
    Dog(){
        System.out.println("I am a Dog");
    }

    Dog (String type){
        this.type = type;
        System.out.println("Some dogs can be dangerous and some are not but it is "+type+"\n");
    }
}

class Elephant extends Animal{
    String type;
    Elephant (String type){
        super(type);    // Now it will call its parent class constructor which takes a String argument
        this.type = type;
        System.out.println("Some elephants can be dangerous and some are not but it is "+type+"\n");
    }
    Elephant(){
        System.out.println("I am an Elephant");
    }
}

class Lion extends Animal{
    Lion(){
        System.out.println("I am a Lion");
    }
}

public class ThisAndSuperKeyword {
    public static void main(String[] args) {
        Dog d1 = new Dog();
        d1.setProperties("Dogi Don", true, false, "I can bark and I am Loyal!");
        d1.getProperties();
        Dog d2 = new Dog("dangerous");

        Elephant e1 = new Elephant();
        e1.setProperties("Gajraj", false, false, "I am so Powerful!");
        e1.getProperties();
        Elephant e2 = new Elephant("not dangerous");

        Lion l1 = new Lion();
        l1.setProperties("Shera", false, true, "I am the king of the Jungle!");
        l1.getProperties();
    }
}
