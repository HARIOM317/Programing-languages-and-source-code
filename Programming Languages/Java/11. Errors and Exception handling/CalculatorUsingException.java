class InvalidInputException extends Exception{
    @Override
    public String toString() {
        return "InvalidInputException";
    }

    @Override
    public String getMessage() {
        return "invalid input given by user!";
    }
}

class ZeroDivisionException extends Exception{
    @Override
    public String toString() {
        return "ZeroDivisionException";
    }

    @Override
    public String getMessage() {
        return "can not divided by zero!";
    }
}

class MaxInputException extends Exception{
    @Override
    public String toString() {
        return "MaxInputException";
    }

    @Override
    public String getMessage() {
        return "reached maximum input";
    }
}

public class CalculatorUsingException {
    public static int add(int a, int b, int ...arr) throws InvalidInputException{
        int sum = a+b;
        for (int element:arr){
            if (element == 0){
                throw new InvalidInputException();
            }
            sum += element;
        }
        return sum;
    }

    public static int subtraction(int a, int b) throws MaxInputException, InvalidInputException{
        if (b>a){
            throw new InvalidInputException();
        }
        if (a >= 1000000){
            throw new MaxInputException();
        }
        return a-b;
    }

    public static int product(int a, int b, int ...arr) throws InvalidInputException{
        if (a <= 0 || b <= 0){
            throw new InvalidInputException();
        }
        int multiplication = a*b;
        for (int element:arr){
            if (element == 0){
                throw new InvalidInputException();
            }
            multiplication *= element;
        }
        return multiplication;
    }

    public static float division(float a, float b) throws InvalidInputException, MaxInputException, ZeroDivisionException{
        if (b > a){
            throw new InvalidInputException();
        }
        if (a >= 5000000 || b >= 500000){
            throw new MaxInputException();
        }
        if (b == 0){
            throw new ZeroDivisionException();
        }
        return a/b;
    }

    public static void main(String[] args) {
        try {
            int sum1 = add(5, 9, 14);
            System.out.println("Sum1 = "+sum1);
            int sum2 = add(4, 9, 0, 0, 7);
            System.out.println("Sum 2 = "+sum2);
        }
        catch (InvalidInputException e){
            System.out.println(e);
        }

        try {
            int sub1 = subtraction(1500000, 69880);
            System.out.println("Sub1 = "+sub1);
            int sub2 = subtraction(76, 98);
            System.out.println("sub2 = "+sub2);
        }
        catch (MaxInputException | InvalidInputException e){
            System.out.println(e);
        }

        try {
            int ans = product(9, 0, 8, 5);
            System.out.println("Multiplication = "+ans);
        }
        catch (InvalidInputException e){
            System.out.println(e);
        }

        try {
            float ans = division(34, 0);
            System.out.println("Division = "+ans);
        }
        catch (ZeroDivisionException | InvalidInputException | MaxInputException e){
            System.out.println(e);
        }
    }
}
