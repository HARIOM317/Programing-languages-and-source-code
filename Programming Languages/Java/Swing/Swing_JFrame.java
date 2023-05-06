import javax.swing.*;

public class Swing_JFrame {
    public JFrame f1;       // globally creating JFrame instance
    public Swing_JFrame(){      // Constructor
        f1 = new JFrame("Creating Java Swing JFrame");   // creating frame

        f1.setLayout(null);
        f1.setSize(400, 400);
        f1.setVisible(true);
    }
    public static void main(String[] args) {
        Swing_JFrame myFrame = new Swing_JFrame();
    }
}
