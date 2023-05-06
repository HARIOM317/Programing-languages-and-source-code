package mathematics.shape;

public class Ractangle extends Shape{
    public float area() {
        return width * length;
    }

    public float volume() {
        return width * height * length;
    }

    public double diagonal() {
        double w = width * width;
        double l = length * length;
        return Math.sqrt(w + l);
    }
}
