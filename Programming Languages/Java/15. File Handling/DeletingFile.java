import java.io.File;

public class DeletingFile {
    public static void main(String[] args) {
        File myFile = new File("1.txt");
        // deleting file
        if(myFile.delete()){
            System.out.println(myFile.getName() +" deleted successfully!");
        }
        else {
            System.out.println("Something went wrong!");
        }
    }
}
