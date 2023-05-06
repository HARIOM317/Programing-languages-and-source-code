import java.io.File;
import java.io.IOException;

public class CreatingFile {
    public static void main(String[] args) {
        File myFile = new File("myTextFile.txt");
        try {
            // creating a file
            myFile.createNewFile();
            System.out.println("File created successfully!");
        }
        catch (IOException e){
            System.out.println("Unable to create this file!");
        }
    }
}
