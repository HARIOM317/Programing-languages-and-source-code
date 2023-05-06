import java.util.Stack;

public class MyStack {
    public static void main(String[] args) {
        Stack s1 = new Stack();
        Stack<String> s2 = new Stack<String>();

        s1.push("Hariom");
        s1.push("Singh");
        s1.push("Rajput");

        s2.push("All");
        s2.push("is");
        s2.push("Well!");

        System.out.println(s1);
        System.out.println(s2);

        s1.pop();
        s1.pop();

        System.out.println("S1 = "+ s1);
        System.out.println("s1 peek = "+ s1.peek());
        System.out.println("s2 peek = "+ s2.peek());
    }
}
