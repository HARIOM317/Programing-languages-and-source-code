package mathematics.shape;

public class Square extends Shape {
    public float area() {
        return side * side;
    }

    public float volume() {
        return side * side * side;
    }

    public double diagonal() {
        return Math.sqrt(2) * side;
    }
}
