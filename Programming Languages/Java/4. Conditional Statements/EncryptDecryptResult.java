import java.util.Scanner;
public class EncryptDecryptResult {
    public static void main(String[] args) {
        int math = 80;
        int english = 80;
        int hindi = 90;
        int science = 90;
        int socialScience = 100;
        float result = (math+english+hindi+science+socialScience)/5.0f;
        result = result+8.0f;
        float decryptedResult = result-8.0f;

        System.out.println("Type 'encrypt' for encrypt and 'decrypt' for decrypt: ");
        Scanner sc = new Scanner(System.in);
        String encrypt = sc.next();
        if ("encrypt".equals(encrypt)) {
            System.out.println("Result = "+ result);
        }
        else if ("decrypt".equals(encrypt)) {
            System.out.println("Result = "+ decryptedResult);
        }
        else {
            System.out.println("Invalid input");
        }
    }
}
