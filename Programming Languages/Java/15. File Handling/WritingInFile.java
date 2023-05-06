import java.io.FileWriter;
import java.io.IOException;

public class WritingInFile {
    public static void main(String[] args) {
        // writing in a file
        try {
            FileWriter fileWriter = new FileWriter("myTextFile.txt");
            // writing content
            fileWriter.write("This is our first text file which have been created by using java code.\nThis file has been created successfully!\nOkay now byy!");
            System.out.println("Content written successfully!");
            fileWriter.close();     // closing file
        } catch (IOException e){
            System.out.println("Unable to write in this file!");
        }

    }
}
