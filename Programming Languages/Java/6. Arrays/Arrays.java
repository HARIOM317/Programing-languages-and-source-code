public class Arrays {
    public static void main(String[] args) {
        int [] arr = new int[5];
        arr[0] = 100;
        arr[1] = 200;
        arr[2] = 300;
        arr[3] = 400;
        arr[4] = 500;
        System.out.println("Elements of array 1");
        for (int i = 0; i < arr.length; i++){
            System.out.print(arr[i]+" ");
        }

        int[] arr2 = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
        System.out.println("\nElements of array 2");
        for (int i = 0; i < arr2.length; i++){
            System.out.print(arr2[i]+" ");
        }
    }
}
