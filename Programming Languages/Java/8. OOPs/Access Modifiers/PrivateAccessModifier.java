class Car{
    private int sheets;
    private String carName;
    private String carColor;
    private float carPrice;
    private int warrantyInYear;

    // setter method
    public void setDetails(int sheet, String name, String color, float price, int warranty){
        sheets = sheet;
        carName = name;
        carColor = color;
        carPrice = price;
        warrantyInYear = warranty;
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

public class PrivateAccessModifier {
    public static void main(String[] args) {
        Car bmw = new Car();
        Car mahindra = new Car();

        bmw.setDetails(10, "BMW", "Black", 12000000.00f, 5);
        bmw.getDetails();

        mahindra.setDetails(10, "Mahindra Tufan", "white", 1000000.00f, 2);
        mahindra.getDetails();
    }
}
