public class FinallyBlock {
    public static int result(){
        try {
            int a = 50;
            int b = 2;
            int c = a/b;
            return c;
        }
        catch (Exception e){
            System.out.println(e);
        }
        finally {
            // It will always execute
            System.out.println("Cleaning up resources... This is the end of the method!");
        }
        // this will execute only when an Exception occur
        System.out.println("Cleaning up all resources...");
        return -1;
    }
    public static void main(String[] args) {
        int ans = result();
        System.out.println(ans);

        System.out.println("\nStarting an infinite loop");
        int a = 45, b = 5;
        while (true){
            try {
                int c = a/b;
                System.out.println("Result = "+c);
            }
            catch (Exception e){
                System.out.println("Something went wrong...");
                break;
            }
            finally {
                System.out.println("Finally, it's done!");
            }
            b--;
        }
        System.out.println("The loop has been terminated!\n");

        // try and finally without catch
        try {
            System.out.println(76/0);
        }
        finally {
            System.out.println("I am finally!");
        }
    }
}
