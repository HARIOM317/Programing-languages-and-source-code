class Student{
    public int rollNumber;
    public String name;
    public float percentage;

    public void showDetails(){
        System.out.println("Name : "+name);
        System.out.println("Roll Number : "+rollNumber);
        System.out.println("Percentage : "+percentage);
    }
}

public class PublicAccessModifier {
    public static void main(String[] args) {
        Student hsr = new Student();
        hsr.name = "Hariom Singh Rajput";
        hsr.rollNumber = 36;
        hsr.percentage = 89.8f;

        hsr.showDetails();
    }
}
