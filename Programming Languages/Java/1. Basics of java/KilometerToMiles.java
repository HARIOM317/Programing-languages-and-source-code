import java.util.Scanner;
public class KilometerToMiles {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Kilometer = ");
        float km = sc.nextFloat();
        float mile = (float) (km*(0.621371));
        System.out.println("Mile = "+mile);
    }
}
