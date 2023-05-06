public class AverageUsingVarArgs {
    // take at least two integer numbers for calculating average
    static float average(int a, int b, int ...arr){
        int arguments = 2 + arr.length;
        float sum = a+b;
        for (int element: arr){
            sum += element;
        }
        float avg = (sum/arguments);
        return avg;
    }
    public static void main(String[] args) {
        System.out.println("Average of 4, 7, 8, 9, 12 and 20 = "+ average(4,7,8,9,12,20));
        System.out.println("Average of 10, 20 and 30 = "+ average(10,20,30));
        System.out.println("Average of 11, 17, 19, 23, 47, and 71 = "+ average(11,17,19,23,47,71));
    }
}
