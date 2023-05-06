import java.util.ArrayDeque;

public class MyArrayDeque {
    public static void main(String[] args) {
        ArrayDeque<String> ad = new ArrayDeque<String>();

        // adding elements
        ad.add("Hariom");
        ad.add("Abhishek");
        ad.add("Aman");
        ad.add("Ankit");
        ad.add("Pooja");

        System.out.println("ArrayDeque Elements : "+ad);

        ad.clear();
        // throw exception
        ad.addFirst("Ashok");
        ad.addFirst("Pradeep");
        ad.addFirst("Pravin");
        ad.addFirst("Yogendra");

        ad.addLast("Neha");
        ad.addLast("Ajay");
        ad.addLast("Pankaj");
        ad.addLast("Shubham");

        // do not throw exception
        ad.offer("Arjun");
        ad.offerFirst("Nirmal");
        ad.offerLast("Komal");


        ad.removeFirst();
        ad.removeLast();

        System.out.println("New ArrayDeque Elements : "+ ad);
        System.out.println("First element = "+ ad.getFirst());
        System.out.println("Last element = "+ ad.getLast());
        System.out.println("Class = "+ ad.getClass());

        ad.poll();
        ad.pollFirst();
        ad.pollLast();

        System.out.println("After polling : "+ ad);
        System.out.println("Peek = "+ ad.peek());
        System.out.println("Last = "+ ad.peekLast());
    }
}
