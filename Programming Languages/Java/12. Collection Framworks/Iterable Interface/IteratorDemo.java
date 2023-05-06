import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class IteratorDemo {
    public static void main(String[] args) {
        List<String> l1 = new ArrayList<String>();
            l1.add("Hariom");
            l1.add("Abhishek");
            l1.add("Aman");
            l1.add("Ankit");
            l1.add("Ashok");

            // iterator
        Iterator<String> itr = l1.iterator();

        // hasNext() -> It returns false if we have reached the end of the collection, otherwise return true.
        // next() -> Returns the last element in a collection
        // remove() -> Removes the last element returned by the iterator from the collection
        while (itr.hasNext()){
            System.out.println(itr.next()+" ");
        }
    }
}
