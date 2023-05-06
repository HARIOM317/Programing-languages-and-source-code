import java.util.Calendar;
import java.util.TimeZone;

public class MyCalendarClass {
    public static void main(String[] args) {
        Calendar c = Calendar.getInstance();
        System.out.println("Calendar Type : "+ c.getCalendarType());
        System.out.println("Time Zone : "+ c.getTimeZone());
        System.out.println("ID : "+c.getTimeZone().getID());

        System.out.println("Time : "+ c.getTime());
        System.out.println("Date : "+ c.get(Calendar.DATE));
        System.out.println("Month : "+ c.get(Calendar.MONTH));
        System.out.println("Year : "+ c.get(Calendar.YEAR));
        System.out.println("Day of Week : "+ c.get(Calendar.DAY_OF_WEEK));
        System.out.println("Hour : "+ c.get(Calendar.HOUR));
        System.out.println("Minute : "+ c.get(Calendar.MINUTE));
        System.out.println("Second : "+ c.get(Calendar.SECOND));

        System.out.println("24 hour format Time : "+ c.get(Calendar.HOUR_OF_DAY) + ":" + c.get(Calendar.MINUTE) + ":" + c.get(Calendar.SECOND));
    }
}
