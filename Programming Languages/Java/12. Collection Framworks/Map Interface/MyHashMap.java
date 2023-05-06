import java.util.HashMap;
import java.util.Map;

public class MyHashMap {
    public static void main(String[] args) {
        HashMap<Integer, String> hm = new HashMap<Integer, String>();

        hm.put(1, "Hariom");
        hm.put(2, "Abhi");
        hm.put(3, "Aman");
        hm.put(4, "Pooja");
        hm.put(5, "Shubham");

        System.out.println("Size of map : "+ hm.size());
        System.out.println("Map : "+ hm);

        // iterating hashmap
        for (Map.Entry m: hm.entrySet()){
            System.out.println(m.getKey()+" "+m.getValue());
        }
    }
}
