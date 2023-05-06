import mathematics.shape.*;
import mathematics.shape.Circle;
import mathematics.shape.Sphere;
import mathematics.shape.Cylinder;

public class UseShape {
    public static void main(String[] args) {
        Circle c1 = new Circle();
        c1.setRadius(5);
        System.out.println("\nArea of circle = "+c1.area());
        System.out.println("Circumference of circle = "+c1.circumference());
        System.out.println("Diameter of circle = "+c1.diameter());

        Sphere s1 = new Sphere();
        s1.setRadius(8);
        System.out.println("\nArea of sphere = "+s1.area());
        System.out.println("Volume of sphere = "+s1.volume());
        System.out.println("Diameter of sphere = "+s1.diameter());
        System.out.println("Circumference of sphere = "+s1.circumference());

        Cylinder C1 = new Cylinder();
        C1.setRadius(5);
        C1.setHeight(10);
        System.out.println("\nSurface area of cylinder = "+ C1.surfaceArea());
        System.out.println("Volume of cylinder = "+ C1.volume());

    }   
}
