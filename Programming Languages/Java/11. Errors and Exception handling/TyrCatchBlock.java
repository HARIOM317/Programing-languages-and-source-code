public class TyrCatchBlock {
    public static void main(String[] args) {
        int a = 60;
        int b = 0;

        try {
            int c = a/b;
            System.out.println("The result is : "+c);   // exception found!
        }
        catch (Exception e){
            System.out.println("Exception found! "+e);
        }

        int x = 10, y = 3;
        try {
            int z = x/y;
            System.out.println("Result = "+z);  // not any exception found!
        }
        catch (Exception e){
            System.out.println("Exception : "+e);
        }
    }
}
