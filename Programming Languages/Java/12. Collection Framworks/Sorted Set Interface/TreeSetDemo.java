import java.util.Iterator;
import java.util.TreeSet;

public class TreeSetDemo {
    public static void main(String[] args) {
        TreeSet<String> t1 = new TreeSet<String>();

        t1.add("Grass");
        t1.add("Rabbit");
        t1.add("Snack");
        t1.add("Eagle");
        System.out.println(t1);

        Iterator<String> itr = t1.iterator();
        while (itr.hasNext()){
            System.out.println(itr.next());
        }
    }
}
