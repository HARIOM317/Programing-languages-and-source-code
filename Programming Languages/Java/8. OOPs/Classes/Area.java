class FindArea{
    public float rectangle(float width, float height){
        return width*height;
    }

    public float circle(float radius){
        return (float) (3.14*radius*radius);
    }

    public float cube(float side){
        return side*side*side;
    }

    public float square(float side){
        return side*side;
    }
}

public class Area {
    public static void main(String[] args) {
        FindArea area = new FindArea();
        System.out.println("The Area of Rectangle : "+area.rectangle(5,7) + " square meter");
        System.out.println("The Area of Cube : "+area.cube(10) + " square meter");
        System.out.println("The Area of Circle : "+area.circle(15) + " square meter");
        System.out.println("The Area of Square : "+area.square(15) + " square meter");
    }
}
