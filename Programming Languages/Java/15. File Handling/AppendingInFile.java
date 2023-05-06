import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class AppendingInFile {
    public static void main(String[] args) {
        String fileName = "myTextFile.txt";
        try {
            BufferedWriter out = new BufferedWriter(new FileWriter(fileName, true));
            out.write("I am HSR\n");
            System.out.println("Data Appending Successfully!");
            out.close();
        } catch (IOException e){
            System.out.println("Exception Occurred!");
        }
    }
}
