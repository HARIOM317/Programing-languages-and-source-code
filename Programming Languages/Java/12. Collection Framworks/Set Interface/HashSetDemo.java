import java.util.HashSet;

public class HashSetDemo {
    public static void main(String[] args) {
        // HashSet constructors
        HashSet<Integer> hs1 = new HashSet<Integer>();
        HashSet<Integer> hs2 = new HashSet<Integer>(10);
        HashSet<Integer> hs3 = new HashSet<Integer>(10, 0.5f);

        hs1.add(5);
        hs1.add(10);
        hs1.add(15);
        hs1.add(20);
        hs1.add(25);

        hs2.add(10);
        hs2.add(20);
        hs2.add(30);
        hs2.add(40);
        hs2.add(50);

        hs3.add(100);
        hs3.add(200);
        hs3.add(300);
        hs3.add(400);
        hs3.add(500);

        System.out.println(hs1);
        System.out.println(hs2);
        System.out.println(hs3);
    }
}
