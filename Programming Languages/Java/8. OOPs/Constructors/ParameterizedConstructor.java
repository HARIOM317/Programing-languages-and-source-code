class Car{
    private int sheets;
    private String carName;
    private String carColor;
    private float carPrice;
    private int warrantyInYear;

    // parameterized constructor
    public Car(int sheet, String name, String color, float price, int warranty){
        sheets = sheet;
        carName = name;
        carColor = color;
        carPrice = price;
        warrantyInYear = warranty;
    }
    // constructor overloading
    public Car(String name, String color, float price){
        sheets = 6;
        carName = name;
        carColor = color;
        carPrice = price;
        warrantyInYear = 1;
    }

    // getter method
    public void getDetails(){
        System.out.println("The Car Name : "+carName);
        System.out.println("The Available Sheets : "+sheets);
        System.out.println("The Car Price : "+carPrice);
        System.out.println("The Car Color : "+carColor);
        System.out.println("The Car Warranty : "+warrantyInYear+"\n");
    }
}

public class ParameterizedConstructor {
    public static void main(String[] args) {
        // creating object with default arguments
        Car bmw = new Car(10, "BMW S1 100", "Blue", 7500000.00f, 3);
        Car farari = new Car("Farari super sonic x1", "Red", 6000000.00f);

        // calling method
        bmw.getDetails();
        farari.getDetails();
    }
}
