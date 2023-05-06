interface Maths{
    int x = 60;
    int y = 40;
    int addInX(int n);
    int addInY(int n);
    int add(int a, int b);
}

/*
class AnonymousClass implements Maths{
    public void display(){
        System.out.println("Hello");
    }
    @Override
    public int addInX(int n){
        return x+n;
    }
    @Override
    public int addInY(int n){
        return y+n;
    }
    @Override
    public int add(int a, int b){
        return a+b;
    }
}
 */

public class MyAnonymousClass {
    public static void main(String[] args) {
        // AnonymousClass a1 = new AnonymousClass();
        // System.out.println(a1.addInX(70));
        // System.out.println(a1.addInY(85));
        // System.out.println(a1.add(20, 87));
        // a1.display();

        // Anonymous class - we can use this class at once only and it has no name
        Maths obj = new Maths() {
            @Override
            public int addInX(int n) {
                return x+n;
            }

            @Override
            public int addInY(int n) {
                return y+n;
            }

            @Override
            public int add(int a, int b) {
                return a+b;
            }
        };

        System.out.println(obj.addInY(20));
        System.out.println(obj.addInX(20));
        System.out.println(obj.add(20, 30));

    }
}
