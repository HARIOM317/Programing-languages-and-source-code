package mathematics.shape;

public class Sphere extends Shape {
    public double area() {
        return 4 * Math.PI * radius * radius;
    }

    public double volume() {
        return (4 / 3.0) * ((Math.PI) * (radius * radius * radius));
    }

    public float diameter() {
        return radius * radius;
    }

    public double circumference() {
        return 2 * Math.PI * radius;
    }
}
