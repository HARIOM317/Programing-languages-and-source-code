import hsr.Hariom.MyPackage;
import hsr.Hariom.HariomProfession;

public class UseMyPackage {
    public static void main(String[] args) {
        MyPackage p1 = new MyPackage();
        System.out.println("a = " + p1.a); // accessible only public property in world(another package)

        // System.out.println(p1.b); // Not accessible
        // System.out.println(p1.c); // Not accessible
        // System.out.println(p1.d); // Not accessible

        System.out.println("\nUsing Package method:");
        p1.show();

        // creating object of another class
        HariomProfession hp = new HariomProfession();
    }
}
