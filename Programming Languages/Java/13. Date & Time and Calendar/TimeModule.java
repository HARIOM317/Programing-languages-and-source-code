import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;

public class TimeModule {
    public static void main(String[] args) {
        // local date
        LocalDate d = LocalDate.now();
        System.out.println(d);

        // local time
        LocalTime t = LocalTime.now();
        System.out.println(t);

        // local date and time
        LocalDateTime dt = LocalDateTime.now();
        System.out.println(dt);
    }
}
