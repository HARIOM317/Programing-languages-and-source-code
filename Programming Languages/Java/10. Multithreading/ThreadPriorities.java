class MyThr extends Thread{
    public MyThr(String name){
        super(name);
    }
   public void run(){
        float i = 1;
       System.out.println("\nStarting process for "+this.getName());
        while (i<=1000){
            if (i==1000){
                System.out.println("\n \033[93;1m Process completed for "+this.getName());
            }
            System.out.println("\033[96;1m"+i/10+"% completed | Running..... the run() method calling by "+this.getName());
            i++;
        }
   }
}

public class ThreadPriorities {
    public static void main(String[] args) {
        MyThr t1 = new MyThr("Constructor 1");
        MyThr t2 = new MyThr("Constructor 2");
        MyThr t3 = new MyThr("Constructor 3 (IMP)");
        MyThr t4 = new MyThr("Constructor 4");
        MyThr t5 = new MyThr("Constructor 5");

        t3.setPriority(Thread.MAX_PRIORITY);    // Higher priority
        t5.setPriority(Thread.NORM_PRIORITY);   // Normal priority (default priority)
        t1.setPriority(Thread.MIN_PRIORITY);    // Minimum priority
        t2.setPriority(7);

        t1.start();
        t2.start();
        t3.start();
        t4.start();
        t5.start();

        System.out.println("\033[91;2m Priority of t1 = "+t1.getPriority());
        System.out.println("\033[91;2m Priority of t2 = "+t2.getPriority());
        System.out.println("\033[91;2m Priority of t3 = "+t3.getPriority());
        System.out.println("\033[91;2m Priority of t4 = "+t4.getPriority());
        System.out.println("\033[91;2m Priority of t5 = "+t5.getPriority());
    }
}
