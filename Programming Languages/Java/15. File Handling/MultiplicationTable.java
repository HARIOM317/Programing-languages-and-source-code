import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class MultiplicationTable {
    public static void main(String[] args) {
        System.out.println("Enter number for multiplication table : ");
        Scanner sc = new Scanner(System.in);
        double number = sc.nextInt();

        File myFile = new File("multiplicationTable.txt");
        try {
            myFile.createNewFile();
        } catch (IOException e){
            System.out.println("File can not be created!");
        }

        // writing table of given number in a file
        try {
            BufferedWriter out = new BufferedWriter(new FileWriter(myFile, true));
            out.write("Table of "+number+" is : \n");
            for (int i = 1; i <= 10; i++){
                out.write(number+" x "+i +" = "+number*i+"\n");
            }
            out.write("\n");
            System.out.println("The table of "+number+" has been written successfully!");
            out.close();
        } catch (IOException e){
            System.out.println("something went wrong!");
        }
    }
}
