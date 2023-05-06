class First{
    int id;
    String name;
    float salary;
    public void display(){
        System.out.println("\nThis is the first method of my custom java class!");
        System.out.println("My id is : "+ id);
        System.out.println("My name is : "+ name);
        System.out.println("My salary is : "+ salary);
    }
}

public class FirstClass {
    public static void main(String[] args) {
        // Instantiating a new object of First class
        First obj = new First();
        // Sating attributes/properties
        obj.id = 100025;
        obj.name = "Hariom Singh Rajput";
        obj.salary = 20000000;

        System.out.println("Id = "+ obj.id);
        System.out.println("Name = "+ obj.name);
        System.out.println("Salary = "+ obj.salary);
        obj.display();
    }
}
