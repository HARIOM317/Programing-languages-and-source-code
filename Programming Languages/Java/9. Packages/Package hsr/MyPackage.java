package hsr.Hariom;

public class MyPackage {
    public int a = 5;
    protected int b = 10;
    private int c = 20;
    int d = 40;

    public void show(){
        System.out.println("a = "+a);
        System.out.println("b = "+b);
        System.out.println("c = "+c);
        System.out.println("d = "+d);
    }
    public static void main(String[] args) {
        System.out.println("I am My Package class method!");
    }
}
