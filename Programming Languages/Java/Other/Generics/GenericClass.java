// Creating a generic class
class MyGeneric<T1, T2>{
    int val;
    private T1 t1;
    private T2 t2;

    public MyGeneric(int val, T1 t1){
        this.val = val;
        this.t1 = t1;
    }
    public MyGeneric(int val, T1 t1, T2 t2){
        this.val = val;
        this.t1 = t1;
        this.t2 = t2;
    }

    public void setVal(int val){
        this.val = val;
    }
    public void setT1(T1 t1){
        this.t1 = t1;
    }
    public void setT2(T2 t2){
            this.t2 = t2;
    }

    public int getVal(){
        return val;
    }
    public T1 getT1(){
        return t1;
    }
    public T2 getT2(){
        return t2;
    }

    void display(){
        System.out.println("Val = "+val);
        System.out.println("t1 = "+t1);
        System.out.println("t2 = "+t2);
    }
}

public class GenericClass {
    public static void main(String[] args) {
        MyGeneric<String, Float> g1 = new MyGeneric<String, Float>(45, "Hariom Singh Rajput");
        MyGeneric<String, Float> g2 = new MyGeneric<String, Float>(100, "i am an Indian", 500000.00f);

        System.out.println("Displaying using g1 object");
        g1.display();
        System.out.println("\nDisplaying using g2 object");
        g2.display();


        System.out.println();
        g1.setT1("Indian");

        String str = g1.getT1();
        float i = g2.getT2();

        System.out.println(str);
        System.out.println(i);
    }
}
