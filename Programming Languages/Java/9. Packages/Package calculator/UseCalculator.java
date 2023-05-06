import java.util.Scanner;

import calculator.Calc;
import calculator.ScientificCalc;
public class UseCalculator {
    public static void main(String[] args) {
        System.out.println("Calculator Calc class method");
        Calc c1 = new Calc();
        int sum = c1.add(50, 150, 200, 500);
        System.out.println("sum = "+sum);

        System.out.println("\nCalculator ScientificCalc class method");
        ScientificCalc s1 = new ScientificCalc();
        System.out.println("sum = "+ s1.add(10, 20));
        System.out.println("sub = "+ s1.sub(50, 20));
        System.out.println("product = "+s1.product(10, 20, 5, 10));
        System.out.println("power = "+s1.power(2.5f, 5));
        System.out.println("average = "+s1.avg(10, 20, 30, 40, 50, 60, 70, 80, 90, 100));
    }
}
