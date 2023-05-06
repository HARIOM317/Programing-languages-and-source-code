// implementing runnable interface
class RunnableThread1 implements Runnable{
    // it is necessary to implement run method
    public void run(){
        int i = 1;
        System.out.println("\n\nFirst gun has been started successfully!\n");
        while (i<=100){
            System.out.println("Firing gun using class RunnableThread1");
            System.out.println("work completed "+i+"%\n");
            i++;
        }
    }
}

// implementing runnable interface
class RunnableThread2 implements Runnable{
    // it is necessary to implement run method
    public void run() {
        int i = 1;
        System.out.println("\n\nSecond gun has been started successfully!\n");
        while (i <= 100) {
            System.out.println("Firing gun using class RunnableThread2");
            System.out.println("work completed "+i+"%\n");
            i++;
        }
    }
}


public class ThreadUsingRunnableInterface {
    public static void main(String[] args) {
        RunnableThread1 bullet1 = new RunnableThread1();
        Thread gun1 = new Thread(bullet1);

        RunnableThread2 bullet2 = new RunnableThread2();
        Thread gun2 = new Thread(bullet2);

        // both the methods will execute simultaneously
        gun1.start();
        gun2.start();

        // Note : If we call run method directly (gun1.run()) without using start method then first method will be completed after second method will start
        //-> gun1.run();
        //-> gun2.run();
    }
}
