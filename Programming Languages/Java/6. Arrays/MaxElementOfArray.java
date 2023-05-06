public class MaxElementOfArray {
    public static void main(String[] args) {
        int [] arr = {12, 45, 980, 14, 4, 766, 99, 10, 76, 97, 65, 87, 23};
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < arr.length; i++){
            if (arr[i] > max){
                max = arr[i];
            }
        }
        System.out.println("Max element is : "+ max);
    }
}
