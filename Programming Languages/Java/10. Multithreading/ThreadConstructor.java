// Threading by extending Thread class
class MyThread extends Thread{
    // constructors of Thread class
    public MyThread(String name){
        super(name);
    }
    public MyThread(Runnable r, String name){
        super(r, name);
    }

    public void run(){
        System.out.println("Running... the run method of MyThread class!\n");
    }
}

// Threading by implementing Runnable interface
class MyRunnableThread implements Runnable{
    public void run(){
        System.out.println("Running the run method of MyRunnableThread class! \n");
    }
}

public class ThreadConstructor {
    public static void main(String[] args) {
        MyThread t1 = new MyThread("HSR");
        t1.start();

        // Thread methods
        System.out.println("\nMethods for Thread class instance t1 :");

        System.out.println("The ID of the thread t1 is: "+ t1.getId());
        System.out.println("The Name of the thread t1 is: "+ t1.getName());
        System.out.println("The State of the thread t1 is: "+ t1.getState());
        System.out.println("The Priority of the thread t1 is: "+ t1.getPriority());
        System.out.println("The Class of the thread t1 is: "+ t1.getClass());

        // creating constructor for Thread class which takes runnable r1 and String name
        MyRunnableThread r1 = new MyRunnableThread();
        MyThread t2 = new MyThread(r1, "Hariom Singh Rajput");
        t2.start();

        System.out.println("\nMethods for Thread class instance t2 :");

        System.out.println("Name of thread t2 = "+t2.getName());
        System.out.println("Class of thread t2 = "+t2.getClass());
    }
}
