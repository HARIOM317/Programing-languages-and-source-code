import java.util.LinkedList;
import java.util.Queue;

public class QueueDemo {
    public static void main(String[] args) {
        Queue<Integer> q = new LinkedList<>();

        q.add(10);
        q.add(20);
        q.add(30);
        q.add(40);
        q.add(50);

        System.out.println("Element of queue : "+ q);
        System.out.println("Removed element : "+ q.remove());
        System.out.println("Head = "+ q.peek());
        System.out.println("Size of queue : "+ q.size());
    }
}
