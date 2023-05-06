public class VariableArguments {
    // Variable arguments (VarArgs) -> An array with n number of arguments
    static int sum(int ...arr){
        // Available as int[] arr;
        int result = 0;
        for (int element: arr){
            result += element;
        }
        return result;
    }

    static int addition(int number, int ...arr){  // it will take at least one argument (int number)
        int result = number;
        for (int element: arr){
            result += element;
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println("Sum of nothing is : "+ sum());
        System.out.println("Sum of 2, 6 is : "+ sum(2, 6));
        System.out.println("Sum of 2, 8 and 4 is : "+ sum(2, 8, 4));
        System.out.println("Sum of 2, 8, 15 and 5  is : "+ sum(2, 8, 15, 5));
        System.out.println("Sum of 10, 20, 30, 40 and 50  is : "+ sum(10, 20, 30, 40, 50));

        System.out.println("\nAddition of 10 is : "+ addition(10));
        System.out.println("Addition of 2 and 5 is : "+ addition(2, 5));
        System.out.println("Addition of 1, 2 and 5 is : "+ addition(1, 2, 5));
    }
}
