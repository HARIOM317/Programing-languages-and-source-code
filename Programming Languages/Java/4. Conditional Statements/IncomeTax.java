import java.util.Scanner;
public class IncomeTax {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your income : ");
        float income = sc.nextFloat();
        float tax = 0;

        if (income < 500000.0f){
            tax = tax + 0;   // 0% tax on below 5L
        }
        else if (income >= 500000.0f && income < 1000000.0f){
            tax = tax + 0.1f * (income - 500000);   // 10% tax on above 5L
        }
        else if (income >= 1000000.0f && income < 2500000.0f) {
            tax = tax + 0.1f * (1000000 - 500000);  // 10% tax on above 5L
            tax = tax + 0.2f * (income - 1000000);  // 20% tax on above 10L
        }
        else if (income >= 2500000.0f && income < 5000000.0f) {
            tax = tax + 0.1f * (1000000 - 500000);  // 10% tax on above 5L
            tax = tax + 0.2f * (2500000 - 1000000); // 20% tax on above 10L
            tax = tax + 0.25f * (income - 2500000); // 25% tax on above 25L
        }
        else if (income >= 5000000.0f && income < 10000000.0f) {
            tax = tax + 0.1f * (1000000 - 500000);  // 10% tax on above 5L
            tax = tax + 0.2f * (2500000 - 1000000); // 20% tax on above 10L
            tax = tax + 0.25f * (5000000 - 2500000); // 25% tax on above 25L
            tax = tax + 0.3f * (income - 5000000);  // 30% tax on above 50L
        }
        else {
            tax = tax + 0.1f * (1000000 - 500000);  // 10% tax on above 5L
            tax = tax + 0.2f * (2500000 - 1000000); // 20% tax on above 10L
            tax = tax + 0.25f * (5000000 - 2500000); // 25% tax on above 25L
            tax = tax + 0.3f * (10000000 - 5000000);  // 30% tax on above 50L
            tax = tax + 0.4f * (income - 10000000);  // 40% tax on above 1C
        }
        System.out.println("Income Tax = "+ tax);
    }
}
