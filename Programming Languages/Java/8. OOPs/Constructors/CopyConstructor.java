class Student{
    String name;
    int age;
    float marks;

    void printDetails(){
        System.out.println("Name : "+ this.name);
        System.out.println("Age : "+ this.age);
        System.out.println("Marks : "+ this.marks);
    }

    // Copy Constructor
    Student(Student s2){
        this.name = s2.name;
        this.age = s2.age;
        this.marks = s2.marks;
    }

    Student(){
        // Because copy constructor is creating that's why we need to create a default constructor manually for object s1
    }
}

public class CopyConstructor {
    public static void main(String[] args) {
        Student s1 = new Student();
        s1.name = "Hariom";
        s1.age = 18;
        s1.marks = 89.8f;
        System.out.println("\nDetails of student s1");
        s1.printDetails();

        Student s2 = new Student(s1);
        s2.name = "HSR";
        System.out.println("\nDetails of student s2");
        s2.printDetails();
    }
}
