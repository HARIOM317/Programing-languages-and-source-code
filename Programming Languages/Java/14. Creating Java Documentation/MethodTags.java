/**
 * This is class for describing that how we can use method tags in our java docs
 * @author Hariom Singh rajput
 * @version 1.1.0
 */

public class MethodTags {
    // comment for java docs

    /**
     * Hey, It's my main method
     * @param args These are arguments supplied by the command line
     */
    public static void main(String[] args) {
        System.out.println("This is main method");
    }

    /**
     * This is the method for adding integer numbers
     * @param x this is the first parameter of type int
     * @param y this is the second parameter of type int
     * @param arr this is an integer array where you can pass more than two arguments (x and y)
     * @return it returns the sum of all the passing number in this method
     * @throws Exception if x and y both are 0 which makes no sense to add
     * @deprecated This method has been deprecated please use another method or + operator for addition
     */
    public int addition(int x, int y, int ...arr) throws Exception{
        if (x == 0 && y == 0){
            throw new Exception();
        }
        int sum = x+y;
        for (int element:arr){
            sum += element;
        }
        return sum;
    }
}
