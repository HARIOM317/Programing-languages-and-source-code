package mathematics.shape;

public class Cylinder extends Shape {
    public double surfaceArea() {
        return (2 * Math.PI * radius * height) + (2 * Math.PI * radius * radius);
    }

    public double volume() {
        return Math.PI * radius * radius * height;
    }
}
