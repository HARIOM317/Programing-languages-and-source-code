package calculator;

public class Calc {
    public int add(int a, int b, int ...arr){
        int sum = a+b;
        for (int element: arr){
            sum += element;
        }
        return sum;
    }

    public float sub(float a, float b){
        return a-b;
    }

    public int product(int a, int b, int ...arr){
        int multiplication = a*b;
        for (int element: arr){
            multiplication *= element;
        }
        return multiplication;
    }

    public float divide(float a, float b){
        return a/b;
    }
}
