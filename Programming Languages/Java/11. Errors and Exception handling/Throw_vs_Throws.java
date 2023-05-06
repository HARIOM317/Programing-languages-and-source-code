class Negative_Radius_Exception extends Exception{
    @Override
    public String toString() {
        return "NegativeRadiusException";
    }

    @Override
    public String getMessage() {
        return "Radius can not be negative!";
    }
}

// throws keyword is used to give a signal that the method can throw an Exception which you have to handle using try-catch block
// throw keyword is used to throw an Exception

public class Throw_vs_Throws {
    // signal : it can throw the Negative_Radius_Exception
    public static double area(int r) throws Negative_Radius_Exception{
        if (r < 0){
            // throwing Negative_Radius_Exception
            throw new Negative_Radius_Exception();
        }
        return Math.PI*r*r;
    }

    // signal : it can throw the ArithmeticException
    public static int divide(int a, int b) throws ArithmeticException{
        return a/b;
    }
    public static void main(String[] args) {
        try{
            int a = 10;
            int b = 0;
            divide(a, b);
        }
        catch (Exception e){
            System.out.println("Arithmetic Exception");
        }

        try {
            System.out.println(area(-7));
        }
        catch (Negative_Radius_Exception e){
            System.out.println(e);
        }
    }
}
