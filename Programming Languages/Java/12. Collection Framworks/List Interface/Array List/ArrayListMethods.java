import java.util.ArrayList;
import java.util.function.Predicate;

public class ArrayListMethods {
    public static void main(String[] args) {
        ArrayList<Integer> l1 = new ArrayList<>();
        ArrayList<Integer> l2 = new ArrayList<>(10);
        // ArrayList methods
        // 1. add() -> add an element in ArrayLIst at a specific position otherwise add at the last.
        l1.add(10);
        l1.add(23);
        l1.add(25);
        l1.add(0,18);
        l1.add(3,5);

        l2.add(100);
        l2.add(200);
        l2.add(300);
        l2.add(400);
        l2.add(500);
        l2.add(100);
        l2.add(600);

        // 2. addAll() -> Insert all the elements in the specified collection into this list, starting at specified position.
        l1.addAll(l2);

        // iterating ArrayList
        // 3. size() -> return ArrayList length
        // 4. get() -> return element of given index
        for (int i = 0; i < l1.size(); i++){
            System.out.print( l1.get(i)+" ");
        }

        // 5. clear() -> clear all the elements of ArrayList
        System.out.println("\nAfter clear");
        l1.clear();
        for (int element:l1){
            System.out.print(element+", ");
        }

        //  6. contain() -> return true if given element contains the Array List otherwise return false
        System.out.println(l2.contains(98));
        System.out.println(l2.contains(300));

        // 7. indexOf() -> return index of given element otherwise return -1
        System.out.println(l2.indexOf(400));

        // 8. lastIndexOf() -> return last index of given element if it presents more than 2 times in list
        System.out.println("Last index = "+ l2.lastIndexOf(100));

        // 9. remove() -> remove a element of given index
        l2.remove(0);

        // 10. removeIf -> delete all the elements of the collection that satisfy the specified predicate
        Predicate<Integer> pr = a -> (a%300==0);        // Predicate (a condition)
        l2.removeIf(pr);

        for (int e: l2){
            System.out.print(e+" ");
        }

        // 11. isEmpty() -> return true if list is empty otherwise return false
        System.out.println("\n"+l1.isEmpty());
    }
}
