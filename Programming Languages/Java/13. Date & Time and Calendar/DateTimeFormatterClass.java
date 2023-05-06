import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class DateTimeFormatterClass {
    public static void main(String[] args) {
        LocalDateTime dt = LocalDateTime.now();
        System.out.println(dt);

        // format date
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        DateTimeFormatter dtf2 = DateTimeFormatter.ISO_LOCAL_DATE;

        String myDate = dt.format(dtf);     // converting dt into dtf format
        String myDate2 = dt.format(dtf2);   // converting dt into ISO_LOCAL_DATE format

        // printing formatted date
        System.out.println(myDate);
        System.out.println(myDate2);

        DateTimeFormatter dtf3 = DateTimeFormatter.ofPattern("HH:mm:ss-a");
        String myTime = dt.format(dtf3);
        System.out.println(myTime);
    }
}
