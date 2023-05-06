public class ReversingArray {
    public static void main(String[] args) {
        int [] arr = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
        // reversing array
        for (int i = 0; i < arr.length/2; i++){
            int temp = arr[i];
            arr[i] = arr[arr.length-1-i];
            arr[arr.length-1-i] = temp;
        }
        System.out.println("Reverse array is :");
        for (int i = 0; i < arr.length; i++){
            System.out.print(arr[i]+" ");
        }
    }
}
