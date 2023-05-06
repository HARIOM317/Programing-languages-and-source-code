import java.util.PriorityQueue;

public class MyPriorityQueue {
    public static void main(String[] args) {
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>();

        pq.add(100);
        pq.add(200);
        pq.add(300);
        pq.add(400);
        pq.add(500);

        System.out.println("Peek = "+ pq.peek());
        System.out.println("Poll element = "+ pq.poll());
        System.out.println("remove element = "+ pq.remove());

        System.out.println("Now pq = "+ pq);

    }
}
