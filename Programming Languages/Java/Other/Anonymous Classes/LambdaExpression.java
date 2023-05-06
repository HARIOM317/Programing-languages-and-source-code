@FunctionalInterface
interface Drawable{
    public void draw(int width, int height);
}

public class LambdaExpression {
    public static void main(String[] args) {
        // lambda expression
        Drawable d1=(width, height)->{
            System.out.println("Drawing rectangle of "+ width+ "x"+height+ " cm!");
        };
        d1.draw(10, 20);      // calling lambda expression
    }
}
