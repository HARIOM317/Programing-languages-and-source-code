import java.util.Scanner;
public class GradeOfStudent {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // taking subject marks
        System.out.print("Enter marks of math : ");
        byte math = sc.nextByte();
        System.out.print("Enter marks of science : ");
        byte science = sc.nextByte();
        System.out.print("Enter marks of computer science : ");
        byte computerScience = sc.nextByte();
        System.out.print("Enter marks of social science : ");
        byte socialScience = sc.nextByte();
        System.out.print("Enter marks of english : ");
        byte english = sc.nextByte();

        // calculating percentage
        float percent = (math+science+computerScience+socialScience+english)/5f;
        System.out.println("\nPercentage = "+percent);

        // Checking student grade
        if (percent<=100 && percent >= 85){
            System.out.println("Grade : A+");
        }
        else if (percent<85 && percent >= 75){
            System.out.println("Grade : A");
        }
        else if (percent<75 && percent >= 60){
            System.out.println("Grade : B");
        }
        else if (percent<60 && percent >= 45){
            System.out.println("Grade : C");
        }
        else if (percent<45 && percent >= 33){
            System.out.println("Grade : D");
            System.out.println("You are passed only!");
        }
        else if (percent < 33 && percent >= 0) {
            System.out.println("You are fail!");
        }
        else {
            System.out.println("Something went wrong!\nInvalid percentage");
        }
    }
}
