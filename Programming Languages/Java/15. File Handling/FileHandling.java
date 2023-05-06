import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class FileHandling {
    public static void main(String[] args) {
        // creating file
        File myFile = new File("TextFile2.txt");
        try {
            myFile.createNewFile();
            System.out.println("File created successfully!");
        } catch (IOException e){
            System.out.println("Unable to create this file");
        }

        // writing file
        try {
            FileWriter fileWriter = new FileWriter("TextFile2.txt");
            fileWriter.write("Hello friends, Good Morning!");
            System.out.println("Content written successfully!");
            fileWriter.close();
        } catch (IOException e){
            System.out.println("Unable to write in this file");
        }

        // reading file
        try {
            Scanner sc = new Scanner(myFile);
            System.out.println("File content is : ");
            while (sc.hasNextLine()){
                String line = sc.nextLine();
                System.out.println(line);
            }
            sc.close();
        } catch (IOException e){
            System.out.println("Unable to read this file!");
        }

        // deleting file
        File myFile2 = new File("1.txt");
        if (myFile2.delete()){
            System.out.println("File deleted successfully!");
        }
        else {
            System.out.println("Unable to delete this file!");
        }

        // appending in a file
        String filename = "TextFile2.txt";
        try {
            BufferedWriter out = new BufferedWriter(new FileWriter(filename, true));
            out.write("\nI am from India.");
            System.out.println("data has been appended successfully!");
            out.close();
        } catch (IOException e){
            System.out.println("Unable to append this file!");
        }
    }
}
