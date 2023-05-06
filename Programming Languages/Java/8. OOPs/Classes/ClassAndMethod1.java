class Employee{
    int salary;
    String name;
    int id;
    int experience;

    public int getSalary(){
        return salary;
    }
    public String getName(){
        return name;
    }
    public int getId(){
        return id;
    }
    public int getExperience(){
        return experience;
    }
    public void details(){
        System.out.println("Name = "+name);
        System.out.println("Id = "+id);
        System.out.println("Salary = "+salary);
        System.out.println("Experience = "+experience+"\n");
    }
}

public class ClassAndMethod1 {
    public static void main(String[] args) {
        // creating objects of Employee class
        Employee hariom = new Employee();
        Employee abhishek = new Employee();
        Employee ankit = new Employee();

        // setting attributes of hariom
        hariom.name = "Hariom Singh Rajput";
        hariom.id = 1001;
        hariom.salary = 20000000;
        hariom.experience = 10;

        // setting attributes of abhishek
        abhishek.name = "Abhishek Mewada";
        abhishek.id = 1002;
        abhishek.salary = 10000000;
        abhishek.experience = 5;

        // setting attributes of abhishek
        ankit.name = "Ankit Thakur";
        ankit.id = 1003;
        ankit.salary = 5000000;
        ankit.experience = 2;

        hariom.details();
        abhishek.details();

        System.out.println("The Name of Employee is : "+ankit.getName());
        System.out.println("The Salary of Employee is : "+ankit.getSalary());
        System.out.println("The Id of Employee is : "+ankit.getId());
        System.out.println("The Experience of Employee is : "+ankit.getExperience());
    }
}
