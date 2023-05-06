class ThreadClass1 extends Thread{
    public void run(){
        int i = 1;
        System.out.println("\033[92;1m"+ "\n(Method 1) Starting...\n");
        while (i<=100){
            System.out.println("\033[96;1m Running... run method of first class! "+i+"%");
            i++;
        }
    }
}

class ThreadClass2 extends Thread{
    public void run(){
        int i = 1;
        System.out.println("\033[92;1m"+ "\n(Method 2) Starting...\n");
        while (i<=100){
            System.out.println("\033[93;1m Running... run method of second class! "+i+"%");
            i++;
        }
    }
}

public class ThreadMethods {
    public static void main(String[] args) {
        ThreadClass1 t1 = new ThreadClass1();
        ThreadClass2 t2 = new ThreadClass2();

        System.out.println("before start t1 state : "+t1.getState());
        System.out.println("before start t2 state : "+t2.getState());
        System.out.println("The current thread is : "+Thread.currentThread().getState());

        t1.start();
        System.out.println("After starting t1");
        System.out.println("t1 state : "+t1.getState());
        System.out.println("t2 state : "+t2.getState());
        System.out.println("The current thread is : "+Thread.currentThread().getState());

        try {
            Thread.sleep(5000); // delay this process for 5000 milliseconds
            t1.join();  // complete t1.start() method after that start other method execution
        }
        catch (Exception e){
            System.out.println(e);
        }

        t2.start();
        System.out.println("After starting t2");
        System.out.println("t1 state : "+t1.getState());
        System.out.println("t2 state : "+t2.getState());
        System.out.println("The current thread is : "+Thread.currentThread().getState());
    }
}
