import java.util.LinkedList;

public class LinkedListMethods {
    public static void main(String[] args) {
        LinkedList<Integer> l1 = new LinkedList<>();
        LinkedList<Integer> l2 = new LinkedList<>();
        l1.add(5);
        l1.add(15);
        l1.add(289);
        l1.add(45);
        l1.add(10);

        l2.add(10);
        l2.add(20);
        l2.add(30);
        l2.add(40);
        l2.add(50);

        l2.addLast(100);
        l2.addLast(900);
        l2.addFirst(800);

        l1.addAll(l2);
        for (int i = 0; i < l1.size(); i++){
            System.out.print(l1.get(i)+" -> ");
        }
        System.out.println("NULL");

        System.out.println("After clear");
        l1.clear();
        for (int i = 0; i < l1.size(); i++){
            System.out.print(l1.get(i)+" -> ");
        }
        System.out.println("NULL");

        l2.remove(1);
        for (int element:l2){
            System.out.print(element+" ");
        }
        System.out.println();

        System.out.println(l2.contains(500));
        System.out.println(l1.isEmpty());
    }
}
