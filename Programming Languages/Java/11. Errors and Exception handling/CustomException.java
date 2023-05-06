import java.util.Scanner;

class Circle{
    double areaOfCircle(double radius){
        return Math.PI*radius*radius;
    }
}

// custom exception
class NegativeRadiusException extends Exception{
    @Override
    public String toString() {
        return "NegativeRadiusException";
    }
}

public class CustomException {
    public static void main(String[] args) {
        Circle c1 = new Circle();
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter radius of circle");
        double radius = sc.nextDouble();

        if (radius < 0){
            // handling custom exception
            try{
                throw new NegativeRadiusException();
            }
            catch (Exception e){
                System.out.println(e.toString());
                System.out.println("radius can not be negative!");
                e.printStackTrace();
            }
        }
        else {
            System.out.println("Area of Circle = "+c1.areaOfCircle(radius) + " square meter");
        }

    }
}
