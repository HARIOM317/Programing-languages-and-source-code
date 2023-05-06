class MyThread1 extends Thread{
    // Note : It is necessary to use run method inside class if we extend Thread class for threading
    @Override
    public void run(){
        int i = 1;
        System.out.println("\nStart execution of method 1\n");
        while (i <= 100){
            System.out.println("Threading 1 is running...");
            System.out.println("downloading... "+i+"%");
            i++;
        }
    }

    public void hsr(){
        int i = 0;
        while (i < 50){
            System.out.println("\nI am Hariom Singh Rajput!\n");
            i++;
        }
    }
}

class MyThread2 extends Thread{
    // Note : It is necessary to use run method inside class if we extend Thread class for threading
    @Override
    public void run(){
        int i = 1;
        System.out.println("\nStart execution of method 2\n");
        while (i <= 100){
            System.out.println("Threading 2 is running...");
            System.out.println("Other work "+i+"%");
            i++;
        }
    }
}

public class Threading {
    public static void main(String[] args) {
        MyThread1 t1 = new MyThread1();
        MyThread2 t2 = new MyThread2();

        // for starting a thread we use start method, and it will internally call run() method itself.
        // Note : Executing both the run() methods simultaneously (execute sometime run method1 and sometime run method2 while both are not terminated!)
        t1.start();
        t2.start();
        t1.hsr();   // we wil have to call it manually
    }
}
