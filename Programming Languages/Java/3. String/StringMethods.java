import java.util.Scanner;
public class StringMethods {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String myStr1 = "hello";
        String myStr2 = "HELLO";

        // <<< STRING METHODS >>>
        // 1. charAt - return the character at the specified index
        char result = myStr1.charAt(1);
        System.out.println("Character at index 1 : "+result);
        // 2. length - return length of string
        int length = myStr1.length();
        System.out.println("Length = "+length);
        // 3. compareTo - compare two strings lexicographically
        System.out.println("Comparison : "+ myStr1.compareTo(myStr2));
        // 4. compareToIgnoreCase - compare two strings lexicographically and ignoring case difference
        System.out.println("Comparison : "+ myStr1.compareToIgnoreCase(myStr2));
        // 5. concat - Appends a string to the end of the another string
        System.out.println("Concat in myStr1 : "+myStr1.concat(myStr2));
        // 6. contains - checks whether a string contains a sequence of characters or not
        System.out.println("Contains sequence : "+ myStr2.contains("ELL"));     //true
        // 7. endsWith - checks whether a string ends with the specified character or not
        System.out.println("myStr1 ends with lo : "+ myStr1.endsWith("lo"));
        // 8. equals - Checks that two strings are equal or not
        System.out.println("Equals = "+ myStr1.equals(myStr2));
        // 9. isEmpty - checks whether a string is empty or not
        System.out.println("myStr1 isEmpty : "+ myStr1.isEmpty());
        // 10. replace - searches a string for a specified value, and returns a new string where the specified values are replaced
        System.out.println("Replace myStr1 : "+ myStr1.replace('h', 'y'));
        // 11. toLowerCase - convert a string to lower case letters
        System.out.println("toLowerCase myStr2 : "+ myStr2.toLowerCase());
        // 12. toUpperCase - convert a string to upper case letters
        System.out.println("toUpperCase myStr1 : "+ myStr1.toUpperCase());
        // 13. split string - split a string into an array of sub-strings
        String name = "Hariom-Singh-Rajput";
        System.out.println("Split string:");
        String[] arrOfStr = name.split("-");
        for (String i : arrOfStr){
            System.out.println("\t\t\t"+i);
        }
        // 14. trim - removes whitespaces from both ends of a string
        String str = "         Hello, Good     Morning      ";
        System.out.println("Trim str : "+ str.trim());
        // 15. subString - returns a new string which is the substring of a specified string
        System.out.println("substring of name from index 6 to end : "+ name.substring(6));
        System.out.println("substring of name from index 13 to 19 : "+ name.substring(13, 19));     // start index is included and end index is excluded
        // 16. startsWith - checks whether a string ends with the specified character or not
        System.out.println("myStr1 starts with hel : "+ myStr1.startsWith("hel"));
        // 17. indexOf -  return the position of first found occurrence of specified characters in a string
        String demo = "This is a demo code for index of a string method";
        System.out.println("Index of demo : "+ demo.indexOf("demo"));
        // 18. lastIndexOf - returns the last index of the given string
        System.out.println("last index of a : "+ demo.lastIndexOf("a"));
        // 19. equalsIgnoreCase - Checks that two strings are equal or not and ignore case difference
        System.out.println("Equals and ignore case = "+ myStr1.equalsIgnoreCase("HellO"));
    }
}
