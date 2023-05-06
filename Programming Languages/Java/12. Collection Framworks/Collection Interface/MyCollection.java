import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;
import java.util.LinkedList;

public class MyCollection {
    public static void main(String[] args) {
        Collection<String> list = new LinkedList<String>();
        Collection<Integer> arr = new ArrayList<Integer>();

        list.add("Hariom");
        list.add("Aman");
        list.add("Abhishek");
        list.add("Ankit");

        arr.add(10);
        arr.add(20);
        arr.add(30);
        arr.add(40);
        arr.add(50);

        Iterator<String> itr = list.iterator();

        while (itr.hasNext()){
            System.out.print(itr.next()+" ");
        }

        System.out.println("\n");
        for (int element: arr){
            System.out.println("Number : "+element);
        }

    }
}
