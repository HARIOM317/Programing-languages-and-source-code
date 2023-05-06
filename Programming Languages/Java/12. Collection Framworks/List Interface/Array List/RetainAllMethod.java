import java.util.ArrayList;

public class RetainAllMethod {
    public static void main(String[] args) {
        // creating amn empty ArrayList
        ArrayList<String> bag = new ArrayList<String>();

        // Adding elements in bag
        bag.add("Pen");
        bag.add("Pencil");
        bag.add("Copy");
        bag.add("Book");
        bag.add("Paper");
        bag.add("Bottle");

        // creating another array list
        ArrayList<String> box = new ArrayList<String>();

        // adding elements
        box.add("Pen");
        box.add("Pencil");
        box.add("Rubber");

        System.out.println("Bag contains : "+ bag);
        System.out.println("Box contains : "+ box);

        box.retainAll(bag);

        System.out.println("\nAfter applying retainAll() method");
        System.out.println("bag contains : "+bag);
        System.out.println("box contains : "+box);
    }
}
