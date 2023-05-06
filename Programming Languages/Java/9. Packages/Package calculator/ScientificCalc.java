package calculator;

public class ScientificCalc {
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

    public float avg(int a, int b, int ...arr){
        float sum = a + b;
        for (int element: arr){
            sum += element;
        }
        float average = sum/(arr.length + 2);
        return average;
    }

    public float power(float a, float n){
        float pow = 1;
        if (n == 0){
            return 1;
        }
        for (int i = 0; i < n; i++){
            pow = pow*a;
        }
        return pow;
    }
}
