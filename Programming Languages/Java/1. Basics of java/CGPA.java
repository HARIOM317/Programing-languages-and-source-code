import java.util.Scanner;
public class CGPA {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // taking subject marks
        System.out.print("Enter marks of digital system : ");
        byte digitalSystem = sc.nextByte();
        System.out.print("Enter marks of data structure : ");
        byte dataStructure = sc.nextByte();
        System.out.print("Enter marks of OOPs : ");
        byte OPPs = sc.nextByte();
        System.out.print("Enter marks of EEE : ");
        byte EEE = sc.nextByte();
        System.out.print("Enter marks of discrete structure : ");
        byte discreteStructure = sc.nextByte();

        // calculating cgpa
        float percent = (digitalSystem+dataStructure+OPPs+EEE+discreteStructure)/5f;
        float cgpa = percent/10f;
        System.out.println("\nCGPA = "+cgpa);
    }
}
