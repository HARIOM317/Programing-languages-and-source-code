import java.util.Date;  // this package has been deprecated

public class MyDateClass {
    public static void main(String[] args) {
        Date d = new Date();
        System.out.println("Current Time : "+d);
        System.out.println(d.getTime());
        System.out.println(d.getMonth());
        System.out.println(d.getDate());
        System.out.println(d.getDay());
        System.out.println(d.getHours());
        System.out.println(d.getMinutes());
    }
}
