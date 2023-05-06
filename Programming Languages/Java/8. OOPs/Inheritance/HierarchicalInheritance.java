class A1{
    private String name;
    private String mobileNumber;
    private String address;
    private char gender;
    A1(){
        System.out.println("Hi, I am from section A1");
    }

    public void setData(String name, String mobileNumber, String address, char gender){
        this.name = name;
        this.mobileNumber = mobileNumber;
        this.address = address;
        this.gender = gender;
    }

    public void getData(){
        System.out.println("Name : "+name);
        System.out.println("Mobile number : "+mobileNumber);
        System.out.println("Address : "+address);
        System.out.println("Gender : "+gender+"\n");
    }

}

class B1 extends A1{
    B1(){
        System.out.println("Hi, I am from section B1");
    }
}

class C1 extends A1{
    C1(){
        System.out.println("Hi, I am from section C1");
    }
}

class D1 extends A1{
    D1(){
        System.out.println("Hi, I am from section D1");
    }
}

public class HierarchicalInheritance {
    public static void main(String[] args) {
        A1 a1 = new A1();
        a1.setData("Abhishek", "8823076543", "Indore (MP)", 'M');
        a1.getData();

        B1 b1 = new B1();
        b1.setData("Hariom", "9308767972", "Anandipura, Ashta (MP)", 'M');
        b1.getData();

        C1 c1 = new C1();
        c1.setData("Aman", "8765098000", "Sehore (MP)", 'M');
        c1.getData();

        D1 d1 = new D1();
        b1.setData("Pooja", "8805468761", "Bhopal (MP)", 'F');
        b1.getData();
    }
}
