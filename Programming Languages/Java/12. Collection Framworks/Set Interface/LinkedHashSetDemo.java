import java.util.Iterator;
import java.util.LinkedHashSet;

public class LinkedHashSetDemo {
    public static void main(String[] args) {
        LinkedHashSet<String> set = new LinkedHashSet<String>();

        set.add("Lion");
        set.add("Tiger");
        set.add("Elephant");
        set.add("Got");
        set.add("Dear");
        set.add("Cow");

        System.out.println(set);

        // iterating using iterator
        Iterator<String> itr = set.iterator();

        int i = 1;
        while (itr.hasNext()){
            System.out.println(i+ ") "+ itr.next());
            i++;
        }
    }
}
