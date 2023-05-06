class myCylinder{
    private int radius;
    private int height;

    // setter and getter methods
    public void setRadius(int r){
        radius = r;
    }
    public void getRadius(){
        System.out.println("Radius = "+radius +" meter");
    }
    public void setHeight(int h){
        height = h;
    }
    public void getHeight(){
        System.out.println("Height = "+height + " meter");
    }

    // methods
    public double surfaceArea(){
        return (2*Math.PI*radius*radius) + (2*Math.PI*radius*height);
    }
    public double volume(){
        return Math.PI*radius*radius*height;
    }
}

public class Cylinder {
    public static void main(String[] args) {
        myCylinder c1 = new myCylinder();
        c1.setHeight(12);
        c1.setRadius(9);
        c1.getHeight();
        c1.getRadius();
        double area = c1.surfaceArea();
        double volume = c1.volume();
        System.out.println("Surface area of cylinder is : "+area);
        System.out.println("Volume of cylinder is : "+volume);
    }
}
