import java.util.Scanner;

// creating my own Exception class
class MyException extends Exception{
    @Override
    public String toString() {
        return "Running toString() method!";
    }

    @Override
    public String getMessage() {
        return "Running getMessage() method!";
    }
}

public class CreateException {
    public static void main(String[] args) {
        int a, b;
        System.out.println("Enter value of a");
        Scanner sc = new Scanner(System.in);
        a = sc.nextInt();

        if (a < 99){
            try {
                throw new MyException();
            }
            catch (Exception e){
                System.out.println(e.getMessage());
                System.out.println(e.toString());
                System.out.println(e);  // run toString() method
                e.printStackTrace();    // track error line number
                System.out.println("Finishing...");
            }
            System.out.println("Finished!");
        }

        System.out.println("Enter value of b");
        b = sc.nextInt();

        if(b==0){
            throw new ArithmeticException("Can not divided by zero");
        }
        else {
            System.out.println("Division = "+a/b);
        }
    }
}
