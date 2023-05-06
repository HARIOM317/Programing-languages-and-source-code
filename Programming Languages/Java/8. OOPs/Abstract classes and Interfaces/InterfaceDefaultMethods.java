// Creating interfaces

// interface 1
interface Camera{
    void takeSnap();
    void recordVideo();

    // creating a private method
    private void filter(){
        System.out.println("The filter has been applied");
    }

    // default method - we can implement default methods inside the interface
    default void portraitMode(){
        filter();   // calling private method filter
        System.out.println("\nPortrait mode is enable now!");
    }
}

// interface 2
interface Wifi{
    String[] getNetworks();
    void connectToNetwork(String network);

}

// interface 3
interface MediaPlayer{
    void playMusic(boolean mode);
    void changeMusic();

    // default method
    // Note - we can override default methods in it's derived class
    default void shuffle(){
        System.out.println("\nEnabled shuffle");
    }
}

// Creating a class
class CellPhone{
    CellPhone(){
        System.out.println("Switching on the phone...");
    }

    void callNumber(int number){
        System.out.println("\nCalling on "+number);
    }

    void pickCall(){
        System.out.println("\nConnecting the call...");
    }

    void calc(int a, int b){
        System.out.println("\nAddition = "+ (a+b));
        System.out.println("Subtraction = "+ (a-b));
        System.out.println("Multiplication = "+ (a*b));
        System.out.println("Division = "+ (a/b));
    }
}

class SmartPhone extends CellPhone implements Camera, Wifi, MediaPlayer{
    SmartPhone(){
        System.out.println("Well come...");
    }

    @Override       // overriding shuffle method which is default method of interface
    public void shuffle(){
        System.out.println("\nListen the best songs as you want using shuffle");
    }

    void calc(int a, int b, int ...arr){
        calc(a, b);     // super class method
        System.out.println("Power = "+ Math.pow(a, b));
        float sum = a+b;
        for (int element:arr){
            sum += element;
        }
        float avg = sum/(arr.length+2);
        System.out.println("Total sum = "+sum);
        System.out.println("Average = "+avg);
    }

    // implementing Camera interface methods
    public void takeSnap(){
        System.out.println("\nTaking snap...");
    }
    public void recordVideo(){
        System.out.println("\nRecording video...");
    }

    // implementing Wi-Fi interface methods
    public String[] getNetworks(){
        System.out.println("\nGetting list of available networks...");
        String[] networkList = {"HSR", "MyWLAN", "Krish", "Abhi", "AlwaysOn", "PJR-5G", "HSR 5G-Pro"};
        return networkList;
    }
    public void connectToNetwork(String network){
        System.out.println("\nConnected throw network "+network+" successfully!");
    }

    // implementing MediaPlayer interface methods
    public void playMusic(boolean mode){
        if (mode){
            System.out.println("\nMusic is Playing");
        }
        else {
            System.out.println("\nMusing is Paused");
        }
    }
    public void changeMusic(){
        System.out.println("\nMusic has been changed!");
    }
}

public class InterfaceDefaultMethods {
    public static void main(String[] args) {
        SmartPhone s1 = new SmartPhone();

        s1.takeSnap();
        s1.recordVideo();
        s1.portraitMode();

        String[] arr = s1.getNetworks();
        for (String item: arr){
            System.out.println(item);
        }
        s1.connectToNetwork("HSR");

        s1.playMusic(true);
        s1.changeMusic();
        s1.shuffle();
        s1.playMusic(false);

        s1.pickCall();
        s1.callNumber(1001001);

        s1.calc(10, 5, 20, 30, 40, 50);
    }
}
