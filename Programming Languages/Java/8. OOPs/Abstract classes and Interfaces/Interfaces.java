// creating interface
interface Bicycle{
    int maxSpeed = 50;      // it is by default final variable

    // these methods are by default abstract
    void applyBreak(int decrement);
    void speedUp(int increment);
}

interface ElectricBicycle{
    void batteryBackup();
    void look();
}

// implementing Bicycle and ElectricBicycle in AvonCycle class
class AvonCycle implements Bicycle, ElectricBicycle{
    //Note : if we are implementing interface methods, then we will have to make it public
    int speed;

    AvonCycle(){
        speed = 20;
        System.out.println("Current speed is : "+ speed);
    }

    public void applyBreak(int decrement){
        System.out.println("Applying the break...");
        speed -= decrement;
        System.out.println("Speed = "+speed);
    }
    public void speedUp(int increment){
        System.out.println("Increasing speed...");
        speed += increment;
        System.out.println("Speed = "+speed);
    }
    public void batteryBackup(){
        System.out.println("This can be run 100 kms after full charging!");
    }
    public void look(){
        System.out.println("This is awesome!");
    }
}

public class Interfaces {
    public static void main(String[] args) {
        AvonCycle a1 = new AvonCycle();
        a1.applyBreak(5);
        a1.speedUp(10);
        // We can create properties in interface
        System.out.println("Max speed is : "+a1.maxSpeed);
        a1.batteryBackup();
        a1.look();

        //Note: We cannot modify the properties in Interfaces as they are final
        // a1.maxSpeed = 60;       // throw an error
    }
}
