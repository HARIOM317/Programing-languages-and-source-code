interface Engine{
    private void startingEngine(){
        System.out.println("Starting engine...");
        System.out.println("car started successfully");
    }
    void engineCC();
    void engineType();
    default void insertKey(){
        System.out.println("key inserted");
        startingEngine();
    }
}

interface Break{
    void breakType();
    void decreaseSpeed(int speed, int decrement);
}

interface Wheel{
    void tairType();
    void tairLife();
}

interface Gear{
    void totalGear();
}

class Car{
    private String name;
    private String color;
    private float price;

    Car(){
        System.out.println("This is the car");
    }

    Car(String name, String color, float price){
        this.name = name;
        this.color = color;
        this.price = price;
    }

    public void getDetails(){
        System.out.println("Name : "+name);
        System.out.println("Color : "+color);
        System.out.println("Price : "+price);
    }

    void maxSpeed(){
        System.out.println("Max speed is : 120 km/h");
    }
    void detectItems(){
        System.out.println("Auto detection is not available");
    }
}

class SmartCar extends Car implements Engine, Break, Wheel, Gear{
    int maxSpeed;
    SmartCar(){
        this.maxSpeed = 350;
    }

    @Override   // overriding interface method
    public void insertKey(){
        System.out.println("Fingerprint matches");
        System.out.println("car started successfully");
    }

    void maxSpeed(){
        System.out.println("Max speed is : "+this.maxSpeed+" km/h");
    }
    void detectItems(){
        System.out.println("Auto detection is available");
    }
    void selfDrive(){
        System.out.println("Self driving is available");
    }

    //interface methods
    public void engineCC(){
        System.out.println("CC = 240");
    }
    public void engineType(){
        System.out.println("Engine type : Diesel engine");
    }
    public void breakType(){
        System.out.println("Break type : Power break");
    }
    public void decreaseSpeed(int speed , int decrement){
        if (speed >= decrement){
            System.out.println("Previews speed : "+speed);
            speed -= decrement;
            System.out.println("Current speed : "+speed);
        }
        else {
            System.out.println("Unwanted action performed!");
        }
    }
    public void tairType(){
        System.out.println("Self treatment tiers");
    }
    public void tairLife(){
        System.out.println("Tier life : 10 years");
    }
    public void totalGear(){
        System.out.println("Total available gears = 7");
    }
}

public class PolymorphismInInterface {
    public static void main(String[] args) {
        // This is a Smart Car but access only it's engine properties and behavior
        Engine engine = new SmartCar();
        engine.insertKey();     // call SmartCar class method (Override method)
        engine.engineType();    // call Engine class method
        engine.engineCC();      // call Engine class method

        // engine.maxSpeed();   // not accessible throw engine

        System.out.println();
        // This is a Smart Car but access only it's break properties and behavior
        Break br = new SmartCar();
        br.decreaseSpeed(140, 50);
        br.breakType();
    }
}
