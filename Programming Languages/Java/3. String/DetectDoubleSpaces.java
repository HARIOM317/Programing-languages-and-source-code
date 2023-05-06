public class DetectDoubleSpaces {
    public static void main(String[] args) {
        String str = "This string contains  double   and triple spaces";
        System.out.println("Index of double space : "+str.indexOf("  "));
        System.out.println("Index of triple space : "+str.indexOf("   "));
        System.out.println("Index of continues four spaces : "+str.indexOf("    "));
    }
}
