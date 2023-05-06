import java.util.Vector;

public class MyVector {
    public static void main(String[] args) {
        Vector<Integer> v1 = new Vector<Integer>();
        v1.add(5);
        v1.add(10);
        v1.add(15);
        v1.add(20);
        v1.add(25);

        for (int i = 0; i < v1.size(); i++){
            System.out.print(v1.get(i)+" ");
        }
    }
}
