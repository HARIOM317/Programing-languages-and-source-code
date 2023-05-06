import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class ReadingFile {
    public static void main(String[] args) {
        // Reading file
        File myFile = new File("myTextFile.txt");
        try {
            Scanner sc = new Scanner(myFile);   // reading file
            while (sc.hasNextLine()){
                String line = sc.nextLine();
                System.out.println(line);   // printing file
            }
            sc.close();
        } catch (IOException e){
            System.out.println("Unable to read the file!");
        }
    }
}
