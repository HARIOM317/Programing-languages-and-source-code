package mathematics.shape;

public class Circle extends Shape{
    public double area() {
        return Math.PI * radius * radius;
    }

    public double circumference() {
        return 2 * Math.PI * radius;
    }

    public float diameter() {
        return 2 * radius;
    }
}
