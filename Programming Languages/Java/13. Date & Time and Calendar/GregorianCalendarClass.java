import java.util.GregorianCalendar;
import java.util.TimeZone;

public class GregorianCalendarClass {
    public static void main(String[] args) {
        GregorianCalendar c = new GregorianCalendar();
        System.out.println(c.isLeapYear(2022));
        System.out.println(c.getTime());
        System.out.println(c.getCalendarType());
        System.out.println(c.getWeekYear());
        System.out.println(c.getWeeksInWeekYear());

        System.out.println(TimeZone.getAvailableIDs()[0]);
        System.out.println(TimeZone.getAvailableIDs()[1]);
        System.out.println(TimeZone.getAvailableIDs()[2]);
        System.out.println(TimeZone.getAvailableIDs()[3]);
        System.out.println(TimeZone.getAvailableIDs()[4]);
        System.out.println(TimeZone.getAvailableIDs()[5]);


    }
}
