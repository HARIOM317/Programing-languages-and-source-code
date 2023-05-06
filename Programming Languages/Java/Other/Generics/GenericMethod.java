public class GenericMethod {
    public static <T> void printArray(T[] inputArray){
        for (T element: inputArray){
            System.out.print(element+"    ");
        }
    }
    public static void main(String[] args) {
        Integer[] intArray = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        Float[] floatArray = {10.0f, 20.0f, 30.5f, 40.5f, 50.0f, 60.0f, 70.25f, 80.25f, 90.0f, 100.125f};
        Character[] charArray = {'I', 'N', 'D', 'I', 'A'};
        String[] stringArray = {"Hariom", "Shubham", "Rohan", "Aman", "Pooja", "Ankit", "Abhishek", "Raj"};

        // calling generic method for different types of array
        System.out.println("\n\nInteger Array Contains :");
        printArray(intArray);

        System.out.println("\n\nFloat Array Contains :");
        printArray(floatArray);

        System.out.println("\n\nCharacter Array Contains :");
        printArray(charArray);

        System.out.println("\n\nString Array Contains :");
        printArray(stringArray);
    }
}
