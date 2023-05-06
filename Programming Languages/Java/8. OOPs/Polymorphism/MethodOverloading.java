class Addition{
    int sum(int a, int b){
        return a+b;
    }
    // method overloading
    void sum(float a, float b){
        System.out.println(a+b);
    }

    public int add(int a, int b, int ...arr){
        System.out.println("\nThis is first add method");
        int sum = a+b;
        for (int element:arr){
            sum += element;
        }
        return sum;
    }

    // method overloading
    public float add(float a, float b, float ...arr){
        System.out.println("\nThis is second add method");
        float sum = a+b;
        for (float element: arr){
            sum += element;
        }
        return sum;
    }

    // method overloading
    public void add(int a, int b, float ...arr){
        System.out.println("\nThis is third add method");
        float sum = a+b;
        for (float element: arr){
            sum += element;
        }
        System.out.println("Sum = "+sum);
    }
}

public class MethodOverloading {
    public static void change(int[] arr){
        arr[0] = 50;
        arr[1] = 60;
        arr[2] = 70;
        arr[3] = 80;
    }

    public static void main(String[] args) {
        int [] marks = {89, 75, 91, 65, 89, 100};
        System.out.println("Old value of marks[0] and marks[1] are : "+marks[0]+" and "+marks[1]);
        change(marks);      // the values will be changed because the reference of array is passing here
        System.out.println("New value of marks[0] and marks[1] are : "+marks[0]+" and "+marks[1]);

        Addition num = new Addition();
        System.out.println("Total = "+num.add(2,5));
        System.out.println("Addition = "+num.add(3.0f, 5.4f, 8.9f));
        num.add(6, 10, 5.38f);
    }
}
