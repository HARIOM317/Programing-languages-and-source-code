public class StringBuilderClass {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder("HSR");
        System.out.println(sb);

        // char at index 0
        System.out.println(sb.charAt(0));

        // set char at index 0
        sb.setCharAt(0, 'S');
        System.out.println(sb);

        // insert char at index 0
        sb.insert(0, 'H');
        System.out.println(sb);

        // delete char from index 1 to 3
        sb.delete(1, 3);
        System.out.println(sb);

        // appending character at the last of string
        sb.append("I");     // sb += "I";
        sb.append("T");
        sb.append("I");
        sb.append("K");
        System.out.println(sb);

        // length of string
        System.out.println(sb.length());
    }
}
