import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class JavaGenerics {
    public static void main(String[] args) {
        /*
        // arraylist without declaring its type
        ArrayList arrayList = new ArrayList();
        arrayList.add("String 1");
        arrayList.add(50);
        arrayList.add(950);

        int a = (int)arrayList.get(2);  // we need to typecast it
        System.out.println(a);
         */

        // arraylist with declaring its type
        ArrayList<Integer> arrayList = new ArrayList<>();
        arrayList.add(100);
        arrayList.add(200);
        arrayList.add(300);
        arrayList.add(400);

        System.out.println(arrayList);
        int a = arrayList.get(2);   // do not need to typecast it
        System.out.println(a);

        Map<Integer, String> map = new HashMap<Integer, String>(10);
        map.put(1, "Hariom");
        map.put(2, "Abhishek");
        map.put(3, "Ankit");
        map.put(4, "Aman");
        map.put(5, "Pradeep");

        System.out.println(map);
    }
}
